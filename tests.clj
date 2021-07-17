(ns task.tests
  (:use clojure.test)
  (:require [task.solutions :as t]))


(deftest test-fizzbuzz
  (testing "testing my function"
    (is (= (t/p1-sol 5) [1 2 "FIZZ" 4 "BUZZ"]))))


(deftest test-fibo
  (testing "testing my function"
    (is (= (t/fibo 5) '(1 1 2 3 5) ))))


(deftest test-frequency-count
  (testing "testing my function"
    (is (= (t/word-freq "quick fox lazy dog quick donkey fire fox") {"quick" 2, "fox" 2, "lazy" 1, "dog" 1, "donkey" 1, "fire" 1} ))))
