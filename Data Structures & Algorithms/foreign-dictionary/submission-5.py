class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        graph = {c: set() for w in words for c in w}
        n = len(words)
        in_degree = {c : 0 for c in graph}

        for i in range(n):
            j = i + 1
            if j < n:
                w1 = words[i]
                w2 = words[j]
                n1 = len(words[i])
                n2 = len(words[j])
                k = 0

                while(k < n1 and k < n2 and w1[k] == w2[k]):
                    k += 1

                if (k == n2 and n2 < n1):
                    return ""
                
                if (k != n1):
                    if w2[k] not in graph[w1[k]]:
                        in_degree[w2[k]] += 1
                    graph[w1[k]].add(w2[k])

        res = []

        def dfs(node):
            res.append(node)
            in_degree[node] -= 1

            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    dfs(nei)

        for node in graph:
            if in_degree[node] == 0:
                dfs(node)
            
        return "".join(res) if len(res) == len(graph) else ""
