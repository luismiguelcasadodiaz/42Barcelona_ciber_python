#!/usr/bin7python3

import sys
import os
import traceback
import argparse
from pprint import pprint
"""
Objective
The goal of this exercise is to implement a context manager as a class. 
Thus you are strongly encouraged to do some research about context manager.

Instructions
Implement a CsvReader class that opens, reads, and parses a CSV file. 

This class is then a context manager as class. 

In order to create it, your class requires a few built-in methods:
• __init__,
• __enter__,
• __exit__.
It is mandatory to close the file once the process has completed. 

You are expected to handle properly badly formatted CSV file
 (i.e. handle the exception):
• mistmatch between number of fields and number of records,
• records with different length

CSV (for Comma-Separated Values) file is a delimited text file which uses a
comma to separate values. 

Therefore, the field separator (or delimiter) is usually a comma (,) but
with your context manager you have to OFFER THE POSSIBILITY TO CHANGE this 
parameter.

One can decide if the class instance SKIP LINES

at the top and the bottom of the file
via the parameters skip_top and skip_bottom. 

One should also be able to keep the first
line as a header if header is True.


The file should not be corrupted (either a line with too many values or a line with
too few values), otherwise return None.

You have to handle the case file not found.

You are expected to implement two methods:
• getdata(),
• getheader()

"""

def create_argument_parser():
  def uniform_resource_locator(url_txt):
    """
      helper function that validates url passed at command line
    """
    # 1.- urlparse splits componenst
    parsed_url = urlparse(url_txt)
    # 2.- check if scheme is allowed in this app
    if parsed_url.scheme in ALLOWED_SCHEMES:
      # validators does not accept other schemes than http
      fake_url = "https://" + parsed_url.netloc  
      # 3.- check if netloc/domain/autohity i ok
      ok_url = validators.url(fake_url)
      if not ok_url:
        parser.error("Invalid url {url_txt}")
      else:
        # 4.- returns ALLOWED SCHEME and valid Authuority
        return url_txt

    else:
      # passed scheme is not allowed
      problem1 = parsed_url.scheme
      msg= f"Scheme '{problem1}' from url {url_txt} not allowed"
      parser.error(msg)
  """
    ok_url = validators.url(url_txt)

    if not ok_url:
      parser.error("Invalid url")
    else:
      parsed_url = urlparse(url_txt)
      if parsed_url.scheme in ALLOWED_SCHEMES:
        return url_txt
      else:
        msg= f"Scheme '{parsed_url.scheme}' from url {url_txt} not allowed"
        parser.error(msg)
  """

  def boolean_text(argument):
    """
      helper function check argument passed at command line
    """
    if argument is None:
      return False
    else:
      val = argument.lower()
      if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return True
      elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return False
      else:
        parser.error("{argument} does no realtes to boolean values")

  def positive_integer(argument):
    """
      helper function check argument passed at command line
    """
    if argument is None:
      return 0
    else:
      try:
        int_arg = int(argument)
        if 0 <= int_arg:
          return int_arg
        else:
          parser.error("{argument} number of lines is not positive")
      except:
        parser.error(f"Incorrect number of lines '{argument}'")
      
  
  parser = argparse.ArgumentParser(
    prog='csvreader',
    description='Extraer lineas de ficheros csv',
    epilog='Este es el final de la ayuda'
    )
  
  parser.add_argument('--separator','-s', 
                      help='Values separator character,(Default is: ,)',
                      default=','
                      )

  parser.add_argument('--header', 
                      help='Default is False. If file has headers you must set true',
                      type=boolean_text,
                      default=False)

  parser.add_argument( '--skip-top','-t',
                      help='Número de líneas de datos a saltar al inicio.',
                      type=positive_integer,
                      default=0)
  
  parser.add_argument( '--skip-bottom','-b',
                      help='Número de líneas de datos a ssaltar al inicio.',
                      type=positive_integer,
                      default=0)

  parser.add_argument('filename',
                      help='Fichero CSV a tratar',
                      nargs='+')

  return parser            


class CsvReader():
  def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
      self.filename = filename
      self.sep = sep
      self.header = header  #defines if file has header or not
      self.skip_top = skip_top
      self.skip_bottom = skip_bottom
      self.fd = None
      self.__file_num_lines = None  # i need it to skip_bottom Lines
      
        

  def __enter__(self):
    try:
      count = 0
      with open(self.filename, 'r') as f:
        # read first line to know file template
        line = f.readline()
        count = count + 1
        no_crlf_line = line.strip()
        if no_crlf_line.endswith(self.sep):
          raise ValueError(f"line {count} ends with {self.sep}: RFC4180 2.4")
        file_num_fields = len(no_crlf_line.split(self.sep))
        
        # check if resto of teh lines follow same template
        for line in f:

          count = count + 1

          no_crlf_line = line.strip()
          if no_crlf_line.endswith(self.sep):
            raise ValueError(f"line {count} ends with {self.sep}: RFC4180 2.4")
          
          line_fields_num = len(no_crlf_line.split(self.sep))
          if line_fields_num != file_num_fields:
            msg = f"line {count} does not match first line template"
            msg = msg + ":RFC4180 2.4"
            raise ValueError(msg)

      # the file looks good

      self.__file_num_lines = count
      return self  # return self to be associate to WITH variable
    except FileExistsError:
      return None
    except FileNotFoundError:
      print(f"File {self.filename} not found")
      return None
    except ValueError as e:
      print(e)
      return None
      
  def __exit__(self, exc_ty, exc_val, tb):
      if self.fd is not None:
        self.fd.close()
      if any([exc_ty, exc_val, tb]):
          print(exc_ty, exc_val, tb, sep="\n")
          return False
      else:
          return True
  
  def __str__(self):
      c1 = "File: {}\n".format(self.filename)
      c2 = "Sep : {}\n".format(self.sep)
      c3 = "Head: {}\n".format(self.header)
      c4 = "Stop: {}\n".format(self.skip_top)
      c5 = "sbot: {}\n".format(self.skip_bottom)
      return c1 + c2 + c3 + c4 + c5  
  
  def getdata(self):
      """ Retrieves the data/records from skip_top to skip bottom.
      Return:
      nested list (list(list, list, ...)) representing the data.
      """
      try:
          
        if self.skip_bottom >= self.__file_num_lines:     # user skips more than existing
          msg = f"Can not skip {self.skip_bottom} bottom lines in {self.__file_num_lines} lines."
          raise ValueError(msg)
        if self.skip_top >= self.__file_num_lines:     # user skips more than existing
          msg = f"Can not skip {self.skip_top} top lines in {self.__file_num_lines} lines."
          raise ValueError(msg)
        if self.skip_top + self.skip_bottom >= self.__file_num_lines:
          msg = f"can not skip {self.skip_top} top lines and "
          msg = msg + f"{self.skip_bottom} bottom lines from "
          msg = msg + f"a {self.__file_num_lines} lines file."
          raise ValueError(msg)   
        generator = self.parse()
        result = []
        line_counter = 0
        if self.header:
            # as the file has header
            # i skip it
            next(generator)
            line_counter = line_counter + 1

        for _ in range(self.skip_top):
            next(generator)
            line_counter = line_counter + 1

        for _ in range(line_counter, self.__file_num_lines - self.skip_bottom):
            result.append(next(generator))

        return result
      except ValueError as e:
        print(e)
        raise ValueError
  
  def getheader(self):
    """ Retrieves the header from csv file.
    Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
    """
    if self.header:
      with open(self.filename, 'r') as f:
        header=f.readline().strip()  # removes final \n
        headers = header.split(self.sep)
      return headers
    else:
      return None

  
  def parse(self):
    """ 
    Reads all lines form the file.
    Removes \n end line
    SPlits the line accordingly
    
    """
    with open(self.filename, 'r') as f:
      for line in f:
        yield line.strip().split(self.sep)
      

if __name__ == "__main__":
  try:
    parser = create_argument_parser()
    if len(sys.argv) == 1:
      args = parser.parse_args(['--header','True', '--skip_top', '2', '--skip_bottom','2','good.csv'])
    else:
      args = parser.parse_args(sys.argv[1:])
    cwd = os.getcwd()
    path_file = os.path.join(cwd, args.filename[0])
    with CsvReader(filename=path_file, 
                    sep=args.separator,
                    header= args.header,
                    skip_top=args.skip_top,
                    skip_bottom = args.skip_bottom ) as file:
      if file == None:
        print("File is corrupted")
      else:
        print("-"*80)
        print(file.getheader())
        print("-"*80)
        for line in file.getdata():
          print(line)
  except BaseException as e:
    print(e)
