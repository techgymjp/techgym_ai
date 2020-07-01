# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 01:05:59 2019

@author: n.aoi
"""
from utils import compute_iou_bb

def f1_score(pr, gt, threshold=0.5, verbose=True):
    results = count_tp_fp_fn(pr, gt, threshold)
    tps = results['tps']
    fps = results['fps']
    fns = results['fns']
    if verbose:
        print('TP:', tps, 'FP:', fps, 'FN:', fns)

    if tps+fns==0:
        re = 0
    else:
        re = tps/(tps+fns)
    if tps+fps==0:
        pr = 0
    else:
        pr = tps/(tps+fps)
    if re==0 or pr==0:
        score = 0
    else:
        score = 2*pr*re/(pr+re)

    if verbose:
        print('recall:', re)
        print('precision:', pr)

    return score

def count_tp_fp_fn(pr, gt, threshold=0.5):
    results = {'tps':0, 'fps':0, 'fns':0}
    if len(gt)>0:
        bg = []
        for pred_bb in pr:
            pred_true_dist = [int(compute_iou_bb(pred_bb, true_bb)>=threshold) for true_bb in gt]
            bg.append(pred_true_dist)
        g = GFG(bg)
        mbpm = g.maxBPM()
        results['fps'] += len(pr) -mbpm
        results['fns'] += len(gt) -mbpm
        results['tps'] += mbpm
    else:
        results['fps'] += len(pr)
    return results

def f1_scores(prs, gts):
    results = {'tps':0, 'fps':0, 'fns':0}
    for p, g in zip(prs, gts):
        results = count_tp_fp_fn2(p, g, results)
    tps = results['tps']
    fps = results['fps']
    fns = results['fns']

    if tps+fns==0:
        re = 0
    else:
        re = tps/(tps+fns)
    if tps+fps==0:
        pr = 0
    else:
        pr = tps/(tps+fps)
    if re==0 or pr==0:
        score = 0
    else:
        score = 2*pr*re/(pr+re)
    return score, results

def count_tp_fp_fn2(pr, gt, results, threshold=0.5):
    if len(gt)>0:
        bg = []
        for pred_bb in pr:
            pred_true_dist = [int(compute_iou_bb(pred_bb, true_bb)>=threshold) for true_bb in gt]
            bg.append(pred_true_dist)
        if len(bg) > 0:
            g = GFG(bg)
            mbpm = g.maxBPM()
        else:
            mbpm = 0
        results['fps'] += len(pr) -mbpm
        results['fns'] += len(gt) -mbpm
        results['tps'] += mbpm
    else:
        results['fps'] += len(pr)
    return results

def ap(pr, gt, k=1000, threshold=0.5):
    score = 0
    detected = 0
    num_true = len(gt)
    if num_true>0:
        del_recall = 1/min(num_true, k)
        for i,pred_bb in enumerate(pr):
            if len(gt)>0:
                pred_true_dist = {j:compute_iou_bb(pred_bb, true_bb) for j,true_bb in enumerate(gt)}
                nearest = max(pred_true_dist.items(), key = lambda x:x[1])
                if nearest[1]>=threshold:
                    detected+=1
                    score += detected/(i+1)
                    del gt[nearest[0]]
            else:
                break
        score *= del_recall
    return score

class GFG():
    def __init__(self,graph):
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])

    # A DFS based recursive function
    # that returns true if a matching
    # for vertex u is possible
    def bpm(self, u, matchR, seen):

        # Try every job one by one
        for v in range(self.jobs):

            # If applicant u is interested
            # in job v and v is not seen
            if self.graph[u][v] and seen[v] == False:

                # Mark v as visited
                seen[v] = True

                '''If job 'v' is not assigned to
                   an applicant OR previously assigned
                   applicant for job v (which is matchR[v])
                   has an alternate job available.
                   Since v is marked as visited in the
                   above line, matchR[v]  in the following
                   recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v],
                                               matchR, seen):
                    matchR[v] = u
                    return True
        return False

    # Returns maximum number of matching
    def maxBPM(self):
        '''An array to keep track of the
           applicants assigned to jobs.
           The value of matchR[i] is the
           applicant number assigned to job i,
           the value -1 indicates nobody is assigned.'''
        matchR = [-1] * self.jobs

        # Count of jobs assigned to applicants
        result = 0
        for i in range(self.ppl):

            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs

            # Find if the applicant 'u' can get a job
            if self.bpm(i, matchR, seen):
                result += 1
        return result
