package main

import (
  "io/ioutil"
)

func checkerror(e error) {
  if e != nil {
    panic(e)
  }
}

func checkiswhitespace(src []byte, i *int) bool {
  for *i < len(src) && (src[*i] == 32 || src[*i] == 10) {
    *i++
  }
  return *i == len(src)
}

func checkisnaturalnumber(src []byte, i *int) (bool, bool) {
  j, number := *i, 0
  for j < len(src) && src[j] >= 48 && src[j] <= 57 {
    number = 10*number + int(src[j]) - 48
    j++
  }
  if *i == j {
    return false, *i == len(src)
  }
  *i = j
  print(number)
  return true, *i == len(src)
}

func checkisarithmeticOperator(src []byte, i *int) (bool, bool) {
  if *i < len(src) && src[*i] == 43 {
    *i++
    print("+")
    return true, *i == len(src)
  }
  return false, *i == len(src)
}

func ParseText(filename string) {
  src, e := ioutil.ReadFile(filename)
  checkerror(e)
  i := 0
  for i < len(src) {
    if stop := checkiswhitespace(src, &i); stop {
      continue
    } else if ok, stop := checkisnaturalnumber(src, &i); ok || stop {
      continue
    } else if ok, stop := checkisarithmeticOperator(src, &i); ok || stop {
      continue
    }
  }
  print("\n")
}

func main() {
  ParseText("test.ps")
}