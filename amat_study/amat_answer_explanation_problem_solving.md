# Problem Solving


## Q113PS1

### Step 1: Define the lists
- **List S**: 10 consecutive odd integers.
If the least integer is $a$, then the list is:

$a, a+2, a+4, \dots, a+18$

Average of list S = middle value = $\frac{a + (a+18)}{2} = a+9$.

- **List T**: 5 consecutive even integers.
If the least integer is $b$, then the list is:

$b, b+2, b+4, b+6, b+8$

Average of list T = middle value = $\frac{b + (b+8)}{2} = b+4$.



### Step 2: Relationship between least integers
We’re told:

$a = b + 7$



### Step 3: Difference in averages

$\text{Average of S} - \text{Average of T} = (a+9) - (b+4)$

Substitute $a = b+7$:

$= (b+7+9) - (b+4) = (b+16) - (b+4) = 12$



✅ **Final Answer:**
The average of the integers in list S is **12 greater** than the average of the integers in list T.

---

## Q114PS2


### Step 1: Understand $f(m)$
By definition:

$f(m) = 2 \times 4 \times 6 \times \dots \times m$

for even $m$.

So:

$f(24) = 2 \times 4 \times 6 \times \dots \times 24$



### Step 2: Factorize the structure
Notice each term is even, so we can factor out 2:

$f(24) = 2 \times 4 \times 6 \times \dots \times 24 = 2^{12} \times (1 \times 2 \times 3 \times \dots \times 12)$

That is:

$f(24) = 2^{12} \cdot 12!$



### Step 3: Greatest prime factor
The prime factors of $f(24)$ are the prime factors of $12!$ plus the factor 2.
The largest prime less than or equal to 12 is **11**.

So the greatest prime factor of $f(24)$ is **11**.



✅ **Final Answer:** The greatest prime factor of $f(24)$ is **11**.

---

## Q115PS3



### Step 1: Compute $a$
$a = 1 + \frac{1}{4} + \frac{1}{16} + \frac{1}{64}$

Find a common denominator of 64:

$a = \frac{64}{64} + \frac{16}{64} + \frac{4}{64} + \frac{1}{64} = \frac{85}{64}$

So:

$a = \frac{85}{64}$



### Step 2: Compute $b$

$b = 1 + \frac{a}{4}$

Substitute $a = \frac{85}{64}$:

$b = 1 + \frac{85}{256}$

Convert 1 to denominator 256:

$b = \frac{256}{256} + \frac{85}{256} = \frac{341}{256}$


### Step 3: Compute $a - b$

$a - b = \frac{85}{64} - \frac{341}{256}$

Convert $\frac{85}{64}$ to denominator 256:

$\frac{85}{64} = \frac{340}{256}$

So:

$a - b = \frac{340}{256} - \frac{341}{256} = \frac{-1}{256}$



✅ **Final Answer:**

$a - b = -\frac{1}{256}$

---

## Q116PS4

Let’s solve this step by step:


### Step 1: Current stock
The grocer has **400 pounds** of coffee.
20% is decaffeinated:

$0.20 \times 400 = 80 \text{ pounds decaf}$

So:
- Decaf = 80
- Regular = 320



### Step 2: New purchase
The grocer buys **100 pounds** more.
60% is decaffeinated:

$0.60 \times 100 = 60 \text{ pounds decaf}$

So:
- Decaf = 60
- Regular = 40



### Step 3: Combine totals
Total stock = $400 + 100 = 500$ pounds.
Total decaf = $80 + 60 = 140$ pounds.



### Step 4: Percent decaf

$\frac{140}{500} \times 100 = 28\%$



✅ **Final Answer:**
The grocer’s stock is **28% decaffeinated coffee**.

---



## Q117PS5



### Step 1: Represent shares
Let the common unit be $x$.
- Q’s share = $2x$
- R’s share = $5x$
- S’s share = $8x$

Total profit = $2x + 5x + 8x = 15x$.



### Step 2: Use Q’s actual share
Q’s share = $4,000.
So:

$2x = 4000 \quad \Rightarrow \quad x = 2000$



### Step 3: Find total profit

$15x = 15 \times 2000 = 30{,}000$



✅ **Final Answer:**
The total profit of the business partners was **$30,000**.

---


## Q118PS6


### Step 1: Define variables
Let the number of rooms at Hotel H = $h$.
Then the number of rooms at Hotel G = $2h - 10$.


### Step 2: Use total rooms
We’re told:

$h + (2h - 10) = 425$

Simplify:

$3h - 10 = 425$

$3h = 435$

$h = 145$



### Step 3: Find Hotel G’s rooms

$G = 2h - 10 = 2(145) - 10 = 290 - 10 = 280$



✅ **Final Answer:**
Hotel G has **280 rooms**.

---


## Q119PS7


### Step 1: Recall the definition

$m \, \Theta \, v$ = remainder when $m$ is divided by $v$.



### Step 2: Compute $98 \, \Theta \, 33$
Divide 98 by 33:

$33 \times 2 = 66, \quad 98 - 66 = 32$
So:

$98 \, \Theta \, 33 = 32$



### Step 3: Compute $(98 \, \Theta \, 33) \, \Theta \, 17$
That is $32 \, \Theta \, 17$.
Divide 32 by 17:

$32 - 17 = 15$
So:

$32 \, \Theta \, 17 = 15$



### Step 4: Compute $33 \, \Theta \, 17$
Divide 33 by 17:

$33 - 17 = 16$
So:

$33 \, \Theta \, 17 = 16$



### Step 5: Compute $98 \, \Theta \, (33 \, \Theta \, 17)$
That is $98 \, \Theta \, 16$.
Divide 98 by 16:

$16 \times 6 = 96, \quad 98 - 96 = 2$

So:

$98 \, \Theta \, 16 = 2$



### Step 6: Put it all together

$((98 \, \Theta \, 33) \, \Theta \, 17) - (98 \, \Theta \, (33 \, \Theta \, 17)) = 15 - 2 = 13$



✅ **Final Answer:**
$13$

---

## Q120PS8


### Step 1: Write the five numbers
They are:
1. $ j $
2. $ j + 5 $
3. $ 2j - 1 $
4. $ 4j - 2 $
5. $ 5j - 1 $

---

### Step 2: Compute their sum

$j + (j+5) + (2j-1) + (4j-2) + (5j-1)$

Combine terms:

$= (j + j + 2j + 4j + 5j) + (5 - 1 - 2 - 1)$

$= 13j + 1$



### Step 3: Average condition
The average is 8:

$\frac{13j + 1}{5} = 8$

Multiply both sides by 5:

$13j + 1 = 40$

$13j = 39$

$j = 3$



✅ **Final Answer:**

$j = 3$

---

## Q121PS9



### Step 1: Define Ellen’s sales
Let Ellen = $E$.



### Step 2: Express others in terms of $E$
- Andy = $2E$
- Bob = $E + 3$
- Cary = $2 \times \text{Bob} = 2(E+3) = 2E + 6$
- Dora = Bob + Ellen = $(E+3) + E = 2E + 3$



### Step 3: Compare who sold the most
We now have:
- Andy = $2E$
- Bob = $E + 3$
- Cary = $2E + 6$
- Dora = $2E + 3$
- Ellen = $E$

Clearly, Cary’s sales = $2E + 6$.
Compare with Andy = $2E$: Cary is always 6 more.
Compare with Dora = $2E + 3$: Cary is 3 more.
Compare with Bob and Ellen: Cary is larger for all positive $E$.



✅ **Final Answer:**
**Cary sold the most properties that month.**

---

## Q122PS10

To find the area of the triangular region $BCD$, we can break the problem down into two steps using the Pythagorean theorem and the area formula for a right triangle.


### Step 1: Find the length of the shared side $BD$

First, look at the bottom right triangle, $\triangle ABD$. It is a right triangle with legs $AB = 4$ and $AD = 4$.

Using the Pythagorean theorem ($a^2 + b^2 = c^2$):


$BD^2 = AB^2 + AD^2$

$BD^2 = 4^2 + 4^2$

$BD^2 = 16 + 16 = 32$

$BD = \sqrt{32} = 4\sqrt{2}$


### Step 2: Calculate the area of $\triangle BCD$

Now look at the top triangle, $\triangle BCD$. The square symbol at vertex $B$ indicates that $\angle CBD$ is a right angle ($90^\circ$). This means $\triangle BCD$ is also a right triangle, where the two legs are $BC$ and $BD$.

We are given:

* Base ($BC$) = $4$
* Height ($BD$) = $4\sqrt{2}$

The formula for the area of a triangle is:


$\text{Area} = \frac{1}{2} \times \text{base} \times \text{height}$

Substituting our values:


$\text{Area} = \frac{1}{2} \times 4 \times 4\sqrt{2}$

$\text{Area} = 2 \times 4\sqrt{2} = 8\sqrt{2}$



### Final Answer

The area of the triangular region $BCD$ is **$8\sqrt{2}$** (or approximately **$11.31$** if you need a decimal).

---



## Q123PS11



### Step 1: Playground area
Playground dimensions: $16 \, \text{m} \times 12 \, \text{m}$.

$\text{Area} = 16 \times 12 = 192 \, \text{m}^2$



### Step 2: Garden dimensions
Garden width = 6 m.
Garden area must equal playground area = $192 \, \text{m}^2$.

So length of garden =

$\frac{\text{Area}}{\text{Width}} = \frac{192}{6} = 32 \, \text{m}$



### Step 3: Perimeter of garden
Perimeter formula:

$P = 2(\text{Length} + \text{Width})$

$P = 2(32 + 6) = 2 \times 38 = 76 \, \text{m}$



✅ **Final Answer:**
The perimeter of the rectangular garden is **76 meters**.

---


## Q124PS12


### Step 1: Convert bridge length to miles
Bridge length = 4,024 ft.
Since $1 \, \text{mile} = 5,280 \, \text{ft}$:

$\text{Length in miles} = \frac{4024}{5280} \approx 0.762 \, \text{miles}$



### Step 2: Time to cross at 20 mph
Time (hours) = $\frac{\text{distance}}{\text{speed}} = \frac{0.762}{20} \approx 0.0381 \, \text{hours}$.



### Step 3: Convert hours to minutes

$0.0381 \times 60 \approx 2.29 \, \text{minutes}$



✅ **Final Answer:**
It takes approximately **2.3 minutes** to cross the bridge at 20 mph.

---


## Q125PS13


### Step 1: Cost structure
- First hour = \$12
- Each additional hour = \$3


### Step 2: Total paid
Becky paid \$27.

So after the first hour (\$12), the remaining cost is:

$27 - 12 = 15$



### Step 3: Additional hours
Each additional hour costs \$3, so:

$\frac{15}{3} = 5 \text{ hours}$



### Step 4: Total hours rented

$1 \text{ (first hour)} + 5 \text{ (additional)} = 6 \text{ hours}$



✅ **Final Answer:**
Becky rented the tool for **6 hours**.

---

## Q126PS14



### Step 1: Define ages today
- Rose = $R$
- Sam = $S$
- Tina = $T$

We’re told:
1. $R = 2S$
2. $S = T - 3$ (Sam is 3 years younger than Tina)

---

### Step 2: Ages in 4 years
- Rose = $R + 4$
- Sam = $S + 4$
- Tina = $T + 4$

---

### Step 3: Check each statement

**I. Rose is twice as old as Sam.**
In 4 years:

$R + 4 \stackrel{?}{=} 2(S + 4)$

But originally $R = 2S$. Substituting:

$2S + 4 \stackrel{?}{=} 2S + 8$

This is false (left side is 4 less).
So **Statement I is not necessarily true**.



**II. Sam is 3 years younger than Tina.**
In 4 years:

$(S + 4) = (T + 4) - 3$

Simplify:

$S = T - 3$

Which is exactly the original relationship.
So **Statement II must be true**.



**III. Rose is older than Tina.**
We need to compare $R$ and $T$.
We know $R = 2S$ and $T = S + 3$.
So:

$R - T = 2S - (S + 3) = S - 3$

- If $S > 3$, then $R > T$.
- If $S = 3$, then $R = T$.
- If $S < 3$, then $R < T$.

Since $S$ is a positive integer, this depends on Sam’s age. It is **not guaranteed**.
So **Statement III is not necessarily true**.



### ✅ Final Answer
The only statement that **must** be true in 4 years is:
**II. Sam is 3 years younger than Tina.**

---


## Q127PS15

To find the fraction of the circular region that is shaded, we need to determine the total central angle of the shaded regions.

### 1. Analyze the Angles at Center $O$

* The circle's center is $O$, where two straight lines intersect to form two pairs of vertical angles.
* Vertical angles are equal. Therefore, the unshaded angle opposite the $150^\circ$ angle is also **$150^\circ$**.

### 2. Calculate the Shaded Central Angles

A complete circle contains a total of **$360^\circ$**.

* **Total unshaded central angle:** $150^\circ + 150^\circ = 300^\circ$
* **Total shaded central angle:** $360^\circ - 300^\circ = 60^\circ$

*(Alternatively, because the two shaded sectors are vertical angles, each individual shaded sector has an angle of $30^\circ$, combining for $60^\circ$.)*



### 3. Determine the Fraction

To find what fraction of the entire circle is shaded, divide the shaded angle by the total degrees in a circle:

$\text{Shaded Fraction} = \frac{60^\circ}{360^\circ} = \frac{1}{6}$

The shaded region is **$\frac{1}{6}$** of the circular region.

---

## Q128PS16



### Step 1: Define the profit equation
Profit = Revenue – (Fixed Costs + Variable Costs).

- Fixed costs = \$130,000
- Variable cost per item = \$8
- Selling price per item = \$15
- Desired profit = \$150,000



### Step 2: Express in terms of number of items $x$
Revenue = $15x$
Total cost = $130{,}000 + 8x$
Profit = $15x - (130{,}000 + 8x)$

Simplify:

$\text{Profit} = 15x - 130{,}000 - 8x = 7x - 130{,}000$



### Step 3: Set profit equal to target

$7x - 130{,}000 = 150{,}000$

$7x = 280{,}000$

$x = 40{,}000$



✅ **Final Answer:**
The manufacturer must produce and sell **40,000 items** to earn an annual profit of \$150,000.

---

## Q129PS17

### Step 1: Work rate of the machines
If **4 machines** take **30 hours** to complete the order, then the total work (the order) can be expressed in **machine‑hours**:

$\text{Work} = 4 \times 30 = 120 \text{ machine‑hours}$

So the order requires **120 machine‑hours** of work.



### Step 2: Time with 5 machines
With **5 machines** working together, the time needed is:

$\text{Time} = \frac{\text{Work}}{\text{Machines}} = \frac{120}{5} = 24 \text{ hours}$



### Step 3: Difference in time
Originally: 30 hours.
With 5 machines: 24 hours.
Difference:

$30 - 24 = 6 \text{ hours}$



✅ **Final Answer:**
It takes **6 fewer hours** when all five machines operate simultaneously.

---

## Q130PS18


### Step 1: Mario’s current age
We’re told Mario was **32 years old 8 years ago**.
So today his age is:
$32 + 8 = 40$


### Step 2: Mario’s age $x$ years ago
If Mario is 40 today, then $x$ years ago his age was:

$40 - x$



✅ **Final Answer:**
Mario’s age $x$ years ago was **$40 - x$**.

---


## Q131PS19



### Step 1: Revenue
They produced **500 trucks**, each sold for **\$10**:

$\text{Revenue} = 500 \times 10 = 5{,}000$



### Step 2: Production costs
- First 100 trucks cost \$5 each:

$100 \times 5 = 500$

- Remaining 400 trucks cost \$3.50 each:

$400 \times 3.50 = 1{,}400$

Total cost = $500 + 1{,}400 = 1{,}900$.


### Step 3: Gross profit

$\text{Gross Profit} = \text{Revenue} - \text{Cost} = 5{,}000 - 1{,}900 = 3{,}100$



✅ **Final Answer:**
Company C’s gross profit is **\$3,100**.

---

## Q132PS20

### Definition
The **prime sum** of $n$ = sum of all prime factors of $n$, **with repetitions**.


### Option (A) 440
Factorize:

$440 = 2 \times 2 \times 2 \times 5 \times 11$

Prime sum = $2 + 2 + 2 + 5 + 11 = 22$
👉 Less than 35.


### Option (B) 512
Factorize:

$512 = 2^9$

Prime sum = $2 + 2 + \dots + 2$ (9 times) = $18$
👉 Less than 35.


### Option (C) 620
Factorize:

$620 = 2 \times 2 \times 5 \times 31$

Prime sum = $2 + 2 + 5 + 31 = 40$
👉 Greater than 35 ✅


### Option (D) 700
Factorize:

$700 = 2 \times 2 \times 5 \times 5 \times 7$

Prime sum = $2 + 2 + 5 + 5 + 7 = 21$
👉 Less than 35.



### Option (E) 750
Factorize:

$750 = 2 \times 3 \times 5 \times 5 \times 5$

Prime sum = $2 + 3 + 5 + 5 + 5 = 20$
👉 Less than 35.


### ✅ Final Answer
The integer with prime sum greater than 35 is:
**(C) 620**

---


## Q133PS21


We’re given:

$x = -\tfrac{5}{8}, \quad y = -\tfrac{1}{2}$

Expression:

$-2x - y^2$



### Step 1: Compute $-2x$

$-2x = -2 \times \left(-\tfrac{5}{8}\right) = \tfrac{10}{8} = \tfrac{5}{4}$



### Step 2: Compute $y^2$

$y^2 = \left(-\tfrac{1}{2}\right)^2 = \tfrac{1}{4}$



### Step 3: Put it together

$-2x - y^2 = \tfrac{5}{4} - \tfrac{1}{4} = \tfrac{4}{4} = 1$



✅ **Final Answer:**

$-2x - y^2 = 1$

---

## Q134PS22


### Step 1: Break down spending (excluding tax)
Let Jill’s total spending (before tax) = **100 units** (for simplicity).
- Clothing = 50
- Food = 20
- Other items = 30


### Step 2: Apply tax rates
- Clothing tax = $50 \times 0.04 = 2$
- Food tax = $20 \times 0 = 0$
- Other items tax = $30 \times 0.08 = 2.4$

Total tax = $2 + 0 + 2.4 = 4.4$



### Step 3: Express as percent of total spending

$\frac{4.4}{100} \times 100\% = 4.4\%$



✅ **Final Answer:**
The total tax Jill paid was **4.4%** of her spending, excluding taxes.
**Correct choice: (C)**

---


## Q135PS23



### Step 1: Identify the change
Opening price = \$8
Closing price = \$9
Increase = $9 - 8 = 1$



### Step 2: Percent increase formula

$\text{Percent Increase} = \frac{\text{Increase}}{\text{Original Price}} \times 100\%$

$= \frac{1}{8} \times 100\% = 12.5\%$



✅ **Final Answer:**
The percent increase in the price per share of stock K was **12.5%**.

---

## Q136PS24

### Step 1: Represent the total cost
Total cost = (cost of plants) + (tax on plants) + (shipping).

- Cost per plant = \$3.00
- Sales tax = 5% of plant cost
- Shipping = \$6.95 (flat fee)
- Total cost = \$69.95

Let number of plants = $n$.


### Step 2: Write the equation
Plant cost = $3n$.
Tax = $0.05 \times 3n = 0.15n$.
Shipping = 6.95.

So:

$3n + 0.15n + 6.95 = 69.95$

$3.15n + 6.95 = 69.95$


### Step 3: Solve for $n$

$3.15n = 69.95 - 6.95 = 63$

$n = \frac{63}{3.15} = 20$



✅ **Final Answer:**
Company C ordered **20 plants**.

---

## Q137PS25

We’re given the custom operation:

$s \ast t = (s - 1)(t + 1)$



### Step 1: Substitute $s = -2$

$(-2) \ast x = (-2 - 1)(x + 1) = (-3)(x + 1)$



### Step 2: Set equal to $-12$

$(-3)(x + 1) = -12$



### Step 3: Solve for $x$

$x + 1 = \frac{-12}{-3} = 4$

$x = 4 - 1 = 3$



✅ **Final Answer:**

$x = 3$

---

## Q138PS26


### Step 1: Arrange the set in order

$S = \{0, 2, 4, 5, 8, 11\}$


### Step 2: Find the median
There are 6 numbers (even count).
Median = average of the 3rd and 4th numbers.

$\text{Median} = \frac{4 + 5}{2} = 4.5$



### Step 3: Find the mean

$\text{Mean} = \frac{0 + 2 + 4 + 5 + 8 + 11}{6}$

$= \frac{30}{6} = 5$


### Step 4: Compare mean and median

$\text{Mean} - \text{Median} = 5 - 4.5 = 0.5$



✅ **Final Answer:**
The mean is **0.5 greater** than the median.

---

## Q139PS27


To solve for $k$, 

The given equation is:


$(12^x)(4^{2x+1}) = (2^k)(3^2)$

Since $x$ and $k$ are integers, we can solve this problem by breaking all the bases down into their prime factors ($2$ and $3$) and equating the exponents.

### Step 1: Simplify the Left-Hand Side (LHS)

* **Rewrite $12^x$:**

$12 = 3 \times 2^2 \implies 12^x = (3 \times 2^2)^x = 3^x \times 2^{2x}$


* **Rewrite $4^{2x+1}$:**

$4 = 2^2 \implies 4^{2x+1} = (2^2)^{2x+1} = 2^{2(2x+1)} = 2^{4x+2}$


* **Combine the terms on the LHS:**

$(12^x)(4^{2x+1}) = (3^x \times 2^{2x}) \times (2^{4x+2})$


$= 3^x \times 2^{2x + 4x + 2}$


$= 3^x \times 2^{6x+2}$



### Step 2: Equate LHS to the Right-Hand Side (RHS)

Now, substitute the simplified LHS back into the equation:


$3^x \times 2^{6x+2} = 3^2 \times 2^k$

By the property of unique prime factorization, we can separately equate the exponents of the corresponding bases ($3$ and $2$):

1. **For Base 3:**

$x = 2$


2. **For Base 2:**

$6x + 2 = k$



### Step 3: Solve for $k$

Substitute $x = 2$ into the base 2 exponent equation:


$k = 6(2) + 2$

$k = 12 + 2 = 14$

The value of $k$ is **$14$**.

---

## Q140PS28

### Step 1: Rug area
Rug dimensions = $9 \, \text{ft} \times 12 \, \text{ft}$

$\text{Rug Area} = 9 \times 12 = 108 \, \text{ft}^2$



### Step 2: Relationship to floor area
We’re told the rug covers **60% of the floor area**.
So:

$0.60 \times \text{Floor Area} = 108$



### Step 3: Solve for floor area

$\text{Floor Area} = \frac{108}{0.60} = 180 \, \text{ft}^2$


✅ **Final Answer:**
The area of the floor is **180 square feet**.

---

## Q141PS29


### fast answer

Volume of the tank is $30×20×10 = 6000m^3$.

Tap 1 fills in 60 hours, so $100m^3$ per hour.

Tap 2 fills in 90 hours, so $\frac{200}{3}m^3$ per hour.

Combined inflow rate is $\frac{500}{3}m^3$ per hour.

If there were no holes, it would take $100 + \frac{200}{3} = \frac{500}{3} \approx 166.67\text{ m}^3/\text{hour}$

$\frac{6000}{166.67} = 36 \text{hours}$. Which liminates the first answer A.

There are four holes, one at a height of $2m$, one at a height of $4m$, one at a height of $6m$, an one at a height of $8m$.

From here, there are two ways to approach the rest of the question. The first way is to understand how test-writers design questions, use some logic, test the other extreme (we already tested no holes, so we need to test what happens if all four holes impact the net inflow the entire time), eliminate four answer choices, get the right answer quickly, and move on. The second way is to get bogged down in the actual math to prove the one right answer. I strongly prefer the first way. You do whatever is best for you. 😉

Short solution : -

Maximum rate of filling tank (without any hole) = 6000/60 + 6000/90 = 100 + 200/3 = 500/3 m3 /hr
Minimum time taken to fill the tank (without any hole) = 6000/(500/3) = 36 hours

Minimum rate of filling tank (with all 4 holes) = 6000/60 + 6000/90 - 40 = 100 + 200/3 - 40 = 380/3 m3 /hr
Maximum time taken to fill the tank (with all 4 holes) = 6000/(380/3) = 47.36 hours

Only option B 42 lies between the 2 extremes

### typical answer

To find out how long it will take to fill the tank completely, we need to calculate the volume of the tank, the net rate at which water is entering, and how the outflows through the holes affect the filling process at different heights.

### Step 1: Calculate the Total Volume of the Tank

The dimensions of the base are $30\text{ m} \times 20\text{ m}$ and the height is $10\text{ m}$.

* **Total Volume** = $\text{Length} \times \text{Width} \times \text{Height} = 30 \times 20 \times 10 = 6,000\text{ m}^3$
* **Volume per meter of height** = $30 \times 20 \times 1 = 600\text{ m}^3$
* This means every 2-meter vertical section of the tank has a volume of:

$600\text{ m}^3/\text{m} \times 2\text{ m} = 1,200\text{ m}^3$



### Step 2: Determine the Inflow Rate from the Taps

* **Tap 1 rate** = $\frac{6000\text{ m}^3}{60\text{ hours}} = 100\text{ m}^3/\text{hour}$
* **Tap 2 rate** = $\frac{6000\text{ m}^3}{90\text{ hours}} = \frac{200}{3}\text{ m}^3/\text{hour}$
* **Total Inflow Rate ($R_{\text{in}}$)** = $100 + \frac{200}{3} = \frac{500}{3} \approx 166.67\text{ m}^3/\text{hour}$



### Step 3: Analyze the Outflow Holes

Holes are located every 2 meters along the height ($2\text{ m}$, $4\text{ m}$, $6\text{ m}$, and $8\text{ m}$). A hole only leaks water once the water level reaches or rises past it. Each hole leaks at a rate of $10\text{ m}^3/\text{hour}$.

We can break the filling process into 2-meter height intervals:

#### 1. From 0 meters to 2 meters (Volume = $1,200\text{ m}^3$)

* **Active holes:** 0 (The first hole is at 2m, so no leakage occurs yet).
* **Net Rate:** $\frac{500}{3}\text{ m}^3/\text{hour}$
* **Time taken ($t_1$):** 
$t_1 = \frac{1200}{\frac{500}{3}} = \frac{3600}{500} = 7.2\text{ hours}$



#### 2. From 2 meters to 4 meters (Volume = $1,200\text{ m}^3$)

* **Active holes:** 1 (The hole at 2m is leaking).
* **Total Outflow:** $1 \times 10 = 10\text{ m}^3/\text{hour}$
* **Net Rate:** $\frac{500}{3} - 10 = \frac{470}{3}\text{ m}^3/\text{hour}$
* **Time taken ($t_2$):** 
$t_2 = \frac{1200}{\frac{470}{3}} = \frac{3600}{470} \approx 7.66\text{ hours}$



#### 3. From 4 meters to 6 meters (Volume = $1,200\text{ m}^3$)

* **Active holes:** 2 (Holes at 2m and 4m are leaking).
* **Total Outflow:** $2 \times 10 = 20\text{ m}^3/\text{hour}$
* **Net Rate:** $\frac{500}{3} - 20 = \frac{440}{3}\text{ m}^3/\text{hour}$
* **Time taken ($t_3$):** 
$t_3 = \frac{1200}{\frac{440}{3}} = \frac{3600}{440} \approx 8.18\text{ hours}$



#### 4. From 6 meters to 8 meters (Volume = $1,200\text{ m}^3$)

* **Active holes:** 3 (Holes at 2m, 4m, and 6m are leaking).
* **Total Outflow:** $3 \times 10 = 30\text{ m}^3/\text{hour}$
* **Net Rate:** $\frac{500}{3} - 30 = \frac{410}{3}\text{ m}^3/\text{hour}$
* **Time taken ($t_4$):** 
$t_4 = \frac{1200}{\frac{410}{3}} = \frac{3600}{410} \approx 8.78\text{ hours}$



#### 5. From 8 meters to 10 meters (Volume = $1,200\text{ m}^3$)

* **Active holes:** 4 (Holes at 2m, 4m, 6m, and 8m are leaking).
* **Total Outflow:** $4 \times 10 = 40\text{ m}^3/\text{hour}$
* **Net Rate:** $\frac{500}{3} - 40 = \frac{380}{3}\text{ m}^3/\text{hour}$
* **Time taken ($t_5$):** 
$t_5 = \frac{1200}{\frac{380}{3}} = \frac{3600}{380} \approx 9.47\text{ hours}$



### Step 4: Calculate Total Time

To find the total time required to fill the tank completely, sum up the times taken for each interval:

$\text{Total Time} = t_1 + t_2 + t_3 + t_4 + t_5$

$\text{Total Time} = 7.20 + 7.66 + 8.18 + 8.78 + 9.47 = 41.29\text{ hours}$

It will take approximately **41.3 hours** (or about 41 hours and 17 minutes) to fill the tank completely.

---

## Q142PS30


### Step 1: Define rates
Let the rates of pipes be in **tank/hour**.

- Pipe B = $b$
- Pipe C = 25% less than B → $c = 0.75b$
- Pipe A = $a$

### Step 2: Relation between A+B and C
“A and B together take one third the time taken by C alone.”
That means:

$\frac{1}{a+b} = \frac{1}{3} \cdot \frac{1}{c}$
So:

$a+b = 3c$

### Step 3: Combined rate of all three
All three together fill in 15 hours → rate = $\tfrac{1}{15}$.
So:

$a+b+c = \frac{1}{15}$



### Step 4: Substitute relations
From Step 2: $a+b = 3c$.
So:

$a+b+c = 3c + c = 4c$

$4c = \frac{1}{15} \quad \Rightarrow \quad c = \frac{1}{60}$

### Step 5: Find B and A
- $c = \tfrac{1}{60}$
- Since $c = 0.75b$:

$b = \frac{c}{0.75} = \frac{1/60}{3/4} = \frac{1}{60} \cdot \frac{4}{3} = \frac{4}{180} = \frac{2}{90} = \frac{1}{45}$

- From $a+b = 3c$:

$a+b = 3 \cdot \frac{1}{60} = \frac{1}{20}$

So:

$a = \frac{1}{20} - \frac{1}{45}$



### Step 6: Simplify $a$

$a = \frac{9}{180} - \frac{4}{180} = \frac{5}{180} = \frac{1}{36}$


### Step 7: Time for A alone

$\text{Time} = \frac{1}{a} = 36 \, \text{hours}$



✅ **Final Answer:**
Pipe A alone takes **36 hours** to fill the tank completely.

---

## Q143PS31


### Step 1: Write the average formula

$\text{Average} = \frac{x + y + z}{3}$



### Step 2: Substitute the relation
Since $x + y = 8z$:

$\text{Average} = \frac{8z + z}{3} = \frac{9z}{3}$



### Step 3: Simplify

$\text{Average} = 3z$



✅ **Final Answer:**
The average of $x, y, z$ in terms of $z$ is **$3z$**.

---

## Q144PS32


### Step 1: Given values
- Distance = $2.3 \times 10^{14}$ inches
- Conversion: $1 \, \text{km} \approx 3.9 \times 10^4$ inches


### Step 2: Perform conversion

$\text{Distance in km} = \frac{2.3 \times 10^{14}}{3.9 \times 10^4}$


### Step 3: Simplify

$= \frac{2.3}{3.9} \times 10^{14-4}$

$= 0.59 \times 10^{10}$

$= 5.9 \times 10^9 \, \text{km}$



✅ **Final Answer:**
The average distance is closest to **$5.9 \times 10^9$ km**.
**Correct choice: (B)**

---

## Q145PS33


### Step 1: Truck’s head start
The truck leaves first at 40 mph.
In 1 hour, it covers:

$40 \, \text{miles}$

So when the car starts, the truck is already 40 miles ahead.


### Step 2: Relative speed
Car speed = 60 mph
Truck speed = 40 mph
Relative speed = $60 - 40 = 20 \, \text{mph}$



### Step 3: Time to catch up

$\text{Time} = \frac{\text{Distance ahead}}{\text{Relative speed}} = \frac{40}{20} = 2 \, \text{hours}$



✅ **Final Answer:**
The car will reach the truck **2 hours after leaving the city**.

---

## Q146PS34


$\frac{61.24 \cdot (0.998)^2}{\sqrt{403}}$


### Step 1: Approximate $(0.998)^2$

$(0.998)^2 \approx 0.996$


### Step 2: Multiply numerator

$61.24 \times 0.996 \approx 61.0$



### Step 3: Approximate denominator

$\sqrt{403} \approx 20.07 \quad (\text{since } 20^2 = 400)$


### Step 4: Divide

$\frac{61.0}{20.07} \approx 3.04$



✅ **Final Answer:**
The expression is approximately **3**.
**Correct choice: (B)**

---

## Q147PS35

We want the fraction equal to the decimal $0.0625$.


### Step 1: Recognize the decimal

$0.0625 = \frac{625}{10000}$


### Step 2: Simplify the fraction
Divide numerator and denominator by 625:

$\frac{625}{10000} = \frac{1}{16}$



✅ **Final Answer:**
The decimal $0.0625$ is equal to the fraction **$\tfrac{1}{16}$**.

---


