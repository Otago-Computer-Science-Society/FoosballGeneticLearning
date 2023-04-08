package main

import (
	sys "github.com/Otago-Computer-Science-Society/FoosballGeneticLearning/cmd/main/multiAgentSystem"
	manager "github.com/Otago-Computer-Science-Society/FoosballGeneticLearning/pkg/Manager"
)

func main() {
	targetSystem := sys.MultiAgentSystem{}
	manager := manager.NewManager(&targetSystem, 100, true)
	for generationIndex := 0; generationIndex < 1000; generationIndex++ {
		manager.SimulateGeneration()
	}
}
