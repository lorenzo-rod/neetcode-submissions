class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        graph = {c : set() for w in words for c in w}
        indegree = {c : 0 for c in graph}
        n = len(words)

        for i in range(n):
            j = i + 1
            if j < n:
                w1, w2 = words[i], words[j]
                n1, n2 = len(words[i]), len(words[j])
                k = 0

                while (k < n1 and k < n2 and w1[k] == w2[k]):
                    k += 1
                
                if (k == n2 and n1 > n2):
                    return ""
                
                if (k < n1):
                    if w2[k] not in graph[w1[k]]:
                        indegree[w2[k]] += 1
                        graph[w1[k]].add(w2[k])
                
        path = []

        def dfs(node):
            indegree[node] -= 1

            path.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dfs(nei)
        
        for c in indegree:
            if indegree[c] == 0:
                dfs(c)
        
        return "".join(path) if len(path) == len(graph) else ""


