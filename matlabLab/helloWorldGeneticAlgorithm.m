clc; close all; clear;

populationSize = 100;
genes = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,.-;:_!"#%&/()=?@${[]}';
target = 'Hello, World!';

selectionRate = .1;
crossoverRate = .5;
mutationRate = .1;

maxGenerations = 100;

selectionCount = round(populationSize * selectionRate);
parentCount = round(populationSize * crossoverRate);
childCount = populationSize - selectionCount;
parentThreshold = (1 + mutationRate)/2;

generation = 1;
population = cell(populationSize, 1);
for i = 1:populationSize
    population{i} = randomChromosome(genes, strlength(target));
end
[sortedPopulation, fitnesses] = popFitness(population, target);

log = cell(10, 3);
log = updateLog(log, generation, sortedPopulation{1}, fitnesses(1));
generations = cell(populationSize, maxGenerations);
generations(:, 1) = sortedPopulation;

while (fitnesses(1) < strlength(target) && generation <= maxGenerations)
    [sortedPopulation, fitnesses] = newGeneration(sortedPopulation, fitnesses, selectionCount, parentCount, childCount, mutationRate, parentThreshold, genes, target);
    generation = generation + 1;

    log = updateLog(log, generation, sortedPopulation{1}, fitnesses(1));
    generations(:, generation) = sortedPopulation;
end

for i = 1:size(log, 1)
    if ~isnan(log{i, 1})
        fprintf('Generation: %d, Chromosome: %s, Fitness: %d\n', log{i, 1}, log{i, 2}, log{i, 3});
    end
end
    

function randomAllele = randomAllele(genes)
    r = randi([1, length(genes)], 1);
    randomAllele = genes(r);
end

function randomChromosome = randomChromosome(genes, chromosomeLength)
    randomChromosome = repmat(' ', 1, chromosomeLength);
    for i = 1:chromosomeLength
        randomChromosome(i) = genes(randi([1, length(genes)], 1));
    end
end

function fitness = chromosomeFitness(chromosome, target)
    fitness = sum(chromosome == target);
end

function [population, fitness] = popFitness(population, target)
    fitness = NaN(length(population), 1);
    for i = 1:length(population)
        fitness(i) = chromosomeFitness(population{i}, target);
    end

    [fitness, sortIndex] = sort(fitness, 'descend');
    population = population(sortIndex);
end

function [newPopulation, newFitnesses] = newGeneration(population, fitnesses, selectionCount, parentCount, childCount, mutationRate, parentThreshold, genes, target)
    newPopulation = cell(length(population), 1);
    newPopulation(1:selectionCount) = selection(population, fitnesses, selectionCount, genes);

    parentPopulation = population(1:parentCount);
    newPopulation(selectionCount + 1:end) = crossoverPopulate(parentPopulation, fitnesses, childCount, mutationRate, parentThreshold, genes);

    [newPopulation, newFitnesses] = popFitness(newPopulation, target);
end

function elitePopulation = selection(population, fitnesses, eliteCount, genes)
    elitePopulation = cell(eliteCount, 1);
    for i = 1:eliteCount
        if fitnesses(i) == 0
            elitePopulation{i} = randomChromosome(genes, strlength(population{1}));
        else
            elitePopulation{i} = population{i};
        end
    end
end

function childPopulation = crossoverPopulate(parentPopulation, fitnesses, childrenCount, mutationRate, parentThreshold, genes)
    childPopulation = cell(childrenCount, 1);
    % parentSelection = NaN(childrenCount, 2);
    for i = 1:childrenCount
        [i_1, i_2] = randomUnequalIndecies(length(parentPopulation));

        if(fitnesses(i_1) == 0 || fitnesses(i_2) == 0)
            child = randomChromosome(genes, strlength(parentPopulation{1}));
        else
            parent1 = parentPopulation{i_1};
            parent2 = parentPopulation{i_2};
            child = crossover(parent1, parent2, mutationRate, parentThreshold, genes);
        end

        childPopulation{i} = child;
    end
end

function [i_1, i_2] = randomUnequalIndecies(maxIndex)
    i_1 = randi([1, maxIndex]);
    i_2 = i_1;
    while i_2 == i_1
        i_2 = randi([1, maxIndex]);
    end
end

function child = crossover(parent1, parent2, mutationRate, parentThreshold, genes)
    assert(strlength(parent1) == strlength(parent2), append('parent1 = "', parent1, '" and parent2 = "', parent2, '" dont have the same length'));
    
    child = '';
    for i = 1:strlength(parent1)
        r = rand();
        if r < mutationRate
            child = append(child, randomAllele(genes));
        elseif r < parentThreshold
            child = append(child, parent1(i));
        else
            child = append(child, parent2(i));
        end
    end
end

function updatedLog = updateLog(log, generation, chromosome, fitness)
    updatedLog = log;

    if generation > 10
        updatedLog(6:9, :) = log(7:10, :);
        i = 10;
    else
        i = generation;
    end
    
    updatedLog{i, 1} = generation;
    updatedLog{i, 2} = chromosome;
    updatedLog{i, 3} = fitness;
end