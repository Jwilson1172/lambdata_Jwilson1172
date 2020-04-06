class ProcessingHelper():
    import pandas as pd

    def __init__(self, df: pd.DataFrame) -> type(None):
        """[summary]

        Arguments:
            df {pandas.DataFrame} -- takes a dataframe that you want to do actions to, note that the class
            will hold this df object in a private member object until the getDataFrame() method is called or until
            get_validation_split() is called returning new dataframes
        returns [NoneType] -- private void method does not return anything.
        """
        # set a private atribute to hold the dataframe
        self._dframe = df

    def _check(self):
        """[summary]
        this private method double checks t he user inputed information to see if it makes sense, if it dosent then tell the user that they are dumb
        Raises:
            TypeError: raised if the dataframe object attribute is null
            TypeError: raised if the dt_column attribute is null

        Returns:
            [bool] -- returns a bool that is a synonym of [fail | pass]
            note in the next step if it fails then the program will exit with code 100
        """
        # check to make sure that the dataframe exists and that the column_dt
        # is not blank
        if self._dframe is None:
            raise TypeError(
                "Please specify a DataFrame object when you init ProcessingHelper(df:pandas.DataFrame")
            return False
        if (self.column_dt == "") | (self.column_dt is None):
            raise TypeError(
                "Please make sure that you pass the correct arguments to this method it should be of type <string> or <int>\n\
                which should corospond toa  column in the dataframe that this class was initalized with.\n")
            return False

        # take some time to make sure that the column that is suposed to be in
        # the datafram is infact in that dataframe
        try:
            assert(self.column_dt in self._dframe.columns.to_list())
        except AssertionError as ae:
            print(ae)
            return False
        except ValueError as ve:
            print(ve)
            return False
        return True

    def _add_col(self, col_name: str, data: pandas.Series) -> type(None):
        try:
            self._dframe[col_name] = data
        except Exception as e:
            print(e)
            exit(200)

    def convert_dt(self, column_dt) -> type(None):
        """
        [summary]
        this method will take the name of a column that is know to have tatetime objects that ar5e in object
        form and convert them to DateTime64 form then remove the compoennts from that dt object and store them
        in seperate columns that have the name of the corrosponding component eg 'day','year'...ect

        Arguments:
            column_dt { str | int } -- takes the dataframe column header that points to a column with datatime
            information in it, can be of type int or str as long as that str|int points to a column header in a
            pandas dataframe object that was used to inti the class with
        """
        # make an atribute with the target column so that i can check
        # it with the next command
        self.column_dt = column_dt

        # use the private method check() to see if everything is on
        # the up and up with the df and the arguments that got passed
        # to this method if there is an error then the _cfheck method
        # will give some more information and we will quit here and let
        # the user fix thier error and retry.
        self._check() or exit(100)

        # assuming that there were no errors then I can continue
        # by using the pandas method to_datetime(Series) to convert
        # the dt column into a date time object and add the components
        # as new columns
        self._dframe[column_dt] = pd.to_datetime(self._dframe[column_dt])

        # pull of the the dt components out and save them to new columns in the
        # df
        self._add_col('year', self._dframe[column_dt].dt.year)
        self._add_col('month', self._dframe[column_dt].dt.month)
        self._add_col('day', self._dframe[column_dt].dt.day)
        self._add_col('hour', self._dframe[column_dt].dt.hour)
        self._add_col('minute', self._dframe[column_dt].dt.minute)
        self._add_col('second', self._dframe[column_dt].dt.second)

    def get_validation_split(self, frac=0.2, val_set=True, random_state=42):
        """
        a function to make a validation split in a dataframe.

        Keyword Arguments:
            frac {float} -- the ratio of data to split off in the test set and optiionally the validation set. (default: {0.2})
            val_set {bool} -- toogle the spliting for a validation set (default: {True})
            random_state {int} -- the random seed to use for reproducibility (default: {42})

        Returns:
            [DataFrame] -- this emthod will return a tuple of dataframes for each split that was mad, for insance if you have a validation
            then it will return 3 dataframe objects ina  tuple, if you didn't then it will only return 2
        """
        tr = self._dframe.sample(frac=frac, random_state=random_state)
        t = self._dframe.drop(tr.index)
        if val_set:
            val = tr.sample(frac=frac, random_state=random_state)
            tr = tr.drop(val.index)
            return tr, val, t
        return tr, t

    def getDataFrame(self) -> pd.DataFrame:
        """[summary]
        this function returns a copy of the private datafram that this class stores in memory

        Returns:
            [pandas.DataFrame] -- the private dataframe that this class is holding in memory
        """
        return self._dframe.copy()