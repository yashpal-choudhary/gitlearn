(ns task.solutions
  (:require [clojure.string :as str]))


(defn p1-sol
  [n]
  
  (reduce
   (fn [acc v]
     (cond
       (= v 0) acc
       (= (mod v 5) (mod v 3) 0) (conj acc "FIZZBUZZ")
       (= (mod v 5) 0) (conj acc "BUZZ")
       (= (mod v 3) 0) (conj acc "FIZZ")
       :else (conj acc v)
       )
     )
   [] (range (+ n 1)))
  )


(defn fibo
  ([x]
   (if (= x 1) [1] (fibo x 0 1))
   )
  ([x pre nex]
   (if (= x 0) []
       (cons nex (fibo (dec x) nex (+ pre nex))))))


(defn word-freq
  [s]
  (frequencies (str/split s #" "))
  )

