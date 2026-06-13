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

$$\text{Shaded Fraction} = \frac{60^\circ}{360^\circ} = \frac{1}{6}$$

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



