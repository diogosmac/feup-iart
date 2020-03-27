from ride import Ride


class Dataset(object):

    def __init__(self, filename):
        """
        A Dataset is composed of:
            - a map, defined by the number of rows and columns, as a grid
            - a fleet of vehicles, for which we receive the size
            - a set of scheduled rides
            - a bonus value, which is added to the "score" for each ride that
               starts exactly on time
            - a number of steps, which serves the purpose of counting the passage
               of time as the rides are scheduled and executed
        """

        self.extracted_rides = 0

        self.name = filename
        self.input_str = 'inputs/' + filename + '.in'
        self.output_str = 'outputs/' + filename + '.out'

        with open(self.input_str, 'r') as f:
            """
            The first line holds the dataset values relative to
            the map, number of vehicles, bonus score and amount
            of steps 
            """
            [self.rows, self.cols, self.nvehicles,
             self.nrides, self.bonus, self.steps] = \
                [int(n) for n in f.readline().split()]

            """
            After the initial line, each following line represents
            a scheduled ride
            """
            self.rides = []
            for ride in range(self.nrides):
                self.rides.append(Ride(self.extracted_rides, [int(n) for n in f.readline().split()]))
                self.extracted_rides += 1
