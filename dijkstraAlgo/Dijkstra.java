package dijkstraAlgo;

import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Dijkstra {

    public class DijkstraNode implements Comparable<DijkstraNode>{
        
        private final String name;
        private Integer distance = Integer.MAX_VALUE;
        private List<DijkstraNode> shortestPath = new LinkedList();
        private Map<DijkstraNode, Integer> adjacentNodes = new HashMap<>();
    
        
    
        public DijkstraNode(String name) {
            this.name = name;
        }
    
        public void addAdjacentNode(DijkstraNode node, int weight) {
            adjacentNodes.put(node, weight);
        }
    
        @Override
        public int compareTo(DijkstraNode node) {
            return Integer.compare(this.distance, node.getDistance());
        }
    
        public String getName() {
            return name;
        }
    
        public Integer getDistance() {
            return distance;
        }
    
        public void setDistance(Integer distance) {
            this.distance = distance;
        }
    
        public List<DijkstraNode> getShortestPath() {
            return shortestPath;
        }
    
        public void setShortestPath(List<DijkstraNode> shortestPath) {
            this.shortestPath = shortestPath;
        }
    
        public Map<DijkstraNode, Integer> getAdjacentNodes() {
            return adjacentNodes;
        }
    
        public void setAdjacentNodes(Map<DijkstraNode, Integer> adjacentNodes) {
            this.adjacentNodes = adjacentNodes;
        }
    
    
    }

    public void calculateShortestPath(DijkstraNode source) {
        source.setDistance(0);

        Set<DijkstraNode> settledNodes = new HashSet<>();
        Queue<DijkstraNode> unsettledNodes = new PriorityQueue<>(Collections.singleton(source));
        while (!unsettledNodes.isEmpty()) {
            DijkstraNode currentNode = unsettledNodes.poll();
            currentNode.getAdjacentNodes()
                        .entrySet().stream()
                        .filter(entry -> !settledNodes.contains(entry.getKey()))
                        .forEach(entry -> {
                            evaluateDistanceAndPath(entry.getKey(), entry.getValue(), currentNode);
                            unsettledNodes.add(entry.getKey());
                        });
            settledNodes.add(currentNode);
        }
    }

    private static void evaluateDistanceAndPath(DijkstraNode adjNode, Integer edgeWeight, DijkstraNode source) {
        Integer newDistance = source.getDistance() + edgeWeight;
        if (newDistance < adjNode.getDistance()) {
            adjNode.setDistance(newDistance);
            adjNode.setShortestPath(
                Stream.concat(source.getShortestPath().stream(), Stream.of(source)).toList()
            );
        }
    }

    private static void printPaths(List<DijkstraNode> nodes) {
        nodes.forEach(node -> {
            String path = node.getShortestPath().stream()
                    .map(DijkstraNode::getName)
                    .collect(Collectors.joining(" -> "));
            System.out.println((path.isBlank()
                    ? "%s : %s".formatted(node.getName(), node.getDistance())
                    : "%s -> %s : %s".formatted(path, node.getName(), node.getDistance()))
            );
        });
    }

    public static void main(String[] args) {

        Dijkstra algo = new Dijkstra();
        DijkstraNode nodeA = algo.new DijkstraNode("A");
        DijkstraNode nodeB = algo.new DijkstraNode("B");
        DijkstraNode nodeC = algo.new DijkstraNode("C");
        DijkstraNode nodeD = algo.new DijkstraNode("D");
        DijkstraNode nodeE = algo.new DijkstraNode("E");
        DijkstraNode nodeF = algo.new DijkstraNode("F");

        nodeA.addAdjacentNode(nodeB, 2);
        nodeA.addAdjacentNode(nodeC, 4);

        nodeB.addAdjacentNode(nodeC, 3);
        nodeB.addAdjacentNode(nodeD, 1);
        nodeB.addAdjacentNode(nodeE, 5);

        nodeC.addAdjacentNode(nodeD, 2);

        nodeD.addAdjacentNode(nodeE, 1);
        nodeD.addAdjacentNode(nodeF, 4);

        nodeE.addAdjacentNode(nodeF, 2);

        algo.calculateShortestPath(nodeA);
    }
}


