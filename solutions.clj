<<<<<<< HEAD
(ns task.solutions)


(defn count-word-frequency

  [word wordlist]
  (count (filter #{word} wordlist)))


(defn get-frequency-count

  [wordlist]
  (into {}
        (map #(vector % (count-word-frequency % wordlist))
             (into #{} wordlist))))


(defn first-n-fibonacci
  [n]
  (loop [final '[]
         a  0
         b  1
         count 0]
    (if (= count n)
      final
      (recur (conj final b)
             b
             (+ a b)
             (inc count)))))


(defn get-first-n-fibonacci
  [n]
  (apply list (first-n-fibonacci n)))


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


(defn get-fizzbuzz
  [n]
  (map #(check-fizzbuzz %) (map inc (range n))))
=======
(ns task.solutions
  (:require [clojure.string :as str]))


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

>>>>>>> 5d161ab549d090004a58a3a5de75555a9f7640fa
