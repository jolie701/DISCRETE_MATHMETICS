{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cac2ff3c-3b7b-461d-bcbf-f6ad70d6a004",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter filename:  hw1_input.txt\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "f(x)= 2.2 - 1.8x + 4.0x^3 + 7.0x^4 - 1.03x^5 \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter x value: 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "f( 2.0 )= 109.63999999999999\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter x value: 0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.2\n"
     ]
    }
   ],
   "source": [
    "#-------------------------\n",
    "#This code can run without a problem.\n",
    "#(or, This code CAN NOT run with a detailed explanation about why)\n",
    "\n",
    "#How to run:\n",
    "#1. input the file that contains 2 lines, where line 1 is an integer n; and line 2 contains n+1 real numbers a[0], a[1],..., a[n]\n",
    "#2. it will print out a text like f(x)= a[0] + a[1] x^1 + a[2] x^2 + ... + a[n] x^n\n",
    "#3. it will ask the user to input a value of x, say, b. Then it calculates and outputs f(b)\n",
    "#4. it repeats step 3, unless b=0, which prints out f(0) and STOP\n",
    "\n",
    "#This code is written by Shao-Yun,Chang email h34136091@gs.ncku.edu.tw, on 2026/03/05\n",
    "#-------------------------\n",
    "\n",
    "filename = input(\"Enter filename: \")\n",
    "\n",
    "with open(filename, \"r\") as file:\n",
    "    n = int(file.readline())\n",
    "    line = file.readline()\n",
    "    #把數字用空格切開\n",
    "    parts = line.split()\n",
    "    \n",
    "    #建立一個空list\n",
    "    coeffs = []\n",
    "    #把p='2.2'變成2.2放進list\n",
    "    for p in parts:\n",
    "        coeffs.append(float(p))\n",
    "        \n",
    "\n",
    "#印出f(x)\n",
    "print(\"f(x)=\", end=\" \")\n",
    "#end=\" \" 的意思是不要換行\n",
    "first_term = True\n",
    "#用來判斷是不是第一項，因為第一項前面不能有+\n",
    "\n",
    "l = len(coeffs)\n",
    "for i in range(l):\n",
    "    a = coeffs[i]\n",
    "\n",
    "    if a == 0:\n",
    "        continue #因為題目不要印0項\n",
    "    #處理正負號\n",
    "    if first_term:\n",
    "        if a < 0:\n",
    "            print(\"-\", end=\" \")\n",
    "        first_term = False #代表接下來不是第一項了\n",
    "    else:\n",
    "        if a > 0:\n",
    "            print(\"+\", end=\" \")\n",
    "        else:\n",
    "            print(\"-\", end=\" \")\n",
    "\n",
    "    #印係數(用絕對值)\n",
    "    abs_a = abs(a)\n",
    "\n",
    "    if i == 0:\n",
    "        print(f\"{abs_a}\", end=\" \") #常數項\n",
    "    elif i == 1:\n",
    "        print(f\"{abs_a}x\", end=\" \")\n",
    "    else:\n",
    "        print(f\"{abs_a}x^{i}\", end=\" \")#印出x^i字串\n",
    "\n",
    "print() #換行\n",
    "\n",
    "\n",
    "#計算f(x)，在for外\n",
    "while True:\n",
    "    b = float(input(\"Enter x value:\"))\n",
    "\n",
    "    if b == 0:\n",
    "        print(coeffs[0])\n",
    "        break\n",
    "\n",
    "    result = 0\n",
    "    for i in range(l):\n",
    "        result += coeffs[i]*(b**i)\n",
    "\n",
    "    print(\"f(\",b,\")=\",result)\n",
    "        \n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c835fbd7-d3ab-4004-b8d9-99900bc257fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c7371dc-8f6c-44ec-8b7e-ca595e202283",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
