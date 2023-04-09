package multiagentsystem

import (
	"math"
	"os"
	"testing"
	"time"

	"golang.org/x/exp/rand"

	geneticbreeder "github.com/Otago-Computer-Science-Society/FoosballGeneticLearning/pkg/GeneticBreeder"
	manager "github.com/Otago-Computer-Science-Society/FoosballGeneticLearning/pkg/Manager"
)

func TestMultiAgentSystem(t *testing.T) {
	targetSystem := MultiAgentSystem{}
	geneticBreeder := geneticbreeder.NewGeneticBreeder(
		rand.NewSource(uint64(time.Now().Nanosecond())),
		[]float64{0.0, 0.0, 0.5, 0.5},
		[]float64{0.0, 0.0, 0.0, 0.2, 0.2, 0.2, 0.2, 0.2},
		math.Pow10(-6))
	manager := manager.NewManager(&targetSystem, 100, geneticBreeder, false)
	for generationIndex := 0; generationIndex < 100; generationIndex++ {
		manager.SimulateGeneration()
	}

	os.RemoveAll("data")
	os.RemoveAll("logs")
}
