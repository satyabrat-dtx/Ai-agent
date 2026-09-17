# DB2ADMIN.WRKSALARYWAGEMONTHWISE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 165
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `EMPLOYEECODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 164129

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `WORKMILLNO` | CHAR(6) |  |  |  |  |
| 3 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 4 | `EMPNAME` | VARCHAR(200) |  |  |  |  |
| 5 | `DATEOFJOINING` | DATE |  |  |  |  |
| 6 | `DATEOFLEAVING` | DATE |  |  |  |  |
| 7 | `GENDER` | INTEGER | NOT NULL |  |  |  |
| 8 | `SECTION` | VARCHAR(200) |  |  |  |  |
| 9 | `GRADE` | VARCHAR(200) |  |  |  |  |
| 10 | `DESIGNATION` | VARCHAR(200) |  |  |  |  |
| 11 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 12 | `DAYSWORKED` | DECIMAL(9,5) |  |  |  |  |
| 13 | `WEEKLYOFF` | DECIMAL(9,5) |  |  |  |  |
| 14 | `PAIDLEAVE` | DECIMAL(9,5) |  |  |  |  |
| 15 | `TOTALPAIDHOLIDAYDAYS` | DECIMAL(9,5) |  |  |  |  |
| 16 | `ABSENTDAYS` | DECIMAL(9,5) |  |  |  |  |
| 17 | `UNPAIDWEEKLYOFF` | DECIMAL(9,5) |  |  |  |  |
| 18 | `UNPAIDLEAVEDAYS` | DECIMAL(9,5) |  |  |  |  |
| 19 | `UNPAIDHOLIDAY` | DECIMAL(9,5) |  |  |  |  |
| 20 | `BASIC` | DECIMAL(11,2) |  |  |  |  |
| 21 | `EARNINGHEAD1` | DECIMAL(11,4) |  |  |  |  |
| 22 | `EARNINGHEAD2` | DECIMAL(11,4) |  |  |  |  |
| 23 | `EARNINGHEAD3` | DECIMAL(11,4) |  |  |  |  |
| 24 | `EARNINGTILLLASTHEAD` | DECIMAL(11,4) |  |  |  |  |
| 25 | `DEDUCTIONHEAD1` | DECIMAL(11,4) |  |  |  |  |
| 26 | `DEDUCTIONHEAD2` | DECIMAL(11,4) |  |  |  |  |
| 27 | `DEDUCTIONHEAD3` | DECIMAL(11,4) |  |  |  |  |
| 28 | `DEDUCTIONTILLLASTHEAD` | DECIMAL(11,4) |  |  |  |  |
| 29 | `TOTALEARNING` | DECIMAL(11,4) |  |  |  |  |
| 30 | `TOTALDEDUCTION` | DECIMAL(11,4) |  |  |  |  |
| 31 | `NETPAY` | DECIMAL(11,4) |  |  |  |  |
| 32 | `CATEGORYCODE` | CHAR(10) |  |  |  |  |
| 33 | `EARPAYELEMENT` | CHAR(6) |  |  |  |  |
| 34 | `CATEGORYDESP` | VARCHAR(200) |  |  |  |  |
| 35 | `SUBCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 36 | `DECPAYELEMENT` | CHAR(6) |  |  |  |  |
| 37 | `SUBCATEGORYDESP` | VARCHAR(200) |  |  |  |  |
| 38 | `DIVISIONCODE` | CHAR(10) |  |  |  | Division within a company; second-level organisational discriminator. |
| 39 | `EARPAYELEMENTDESP` | VARCHAR(200) |  |  |  |  |
| 40 | `DIVISIONDESP` | VARCHAR(200) |  |  |  |  |
| 41 | `FACTORYCODE` | CHAR(10) |  |  |  |  |
| 42 | `DEDPAYELEMENTDESP` | VARCHAR(200) |  |  |  |  |
| 43 | `FACTORYDESP` | VARCHAR(200) |  |  |  |  |
| 44 | `DEPARTMENTCODE` | CHAR(10) |  |  |  |  |
| 45 | `EARAMTCALCULATED` | DECIMAL(11,4) |  |  |  |  |
| 46 | `DEPARTMENTDESP` | VARCHAR(200) |  |  |  |  |
| 47 | `SECTIONCODE` | CHAR(6) |  |  |  |  |
| 48 | `DEDAMTCALCULATED` | DECIMAL(11,4) |  |  |  |  |
| 49 | `SECTIONDESP` | VARCHAR(200) |  |  |  |  |
| 50 | `PAYELEMENTBS600DESP` | VARCHAR(200) |  |  |  |  |
| 51 | `PAYELEMENTBS600AMT` | DECIMAL(11,4) |  |  |  |  |
| 52 | `PAYELEMENTSP600DESP` | VARCHAR(200) |  |  |  |  |
| 53 | `PAYELEMENTSPA600DESP` | VARCHAR(200) |  |  |  |  |
| 54 | `PAYELEMENTSSP600DESP` | VARCHAR(200) |  |  |  |  |
| 55 | `PAYELEMENTSP600AMT` | DECIMAL(11,4) |  |  |  |  |
| 56 | `PAYELEMENTSPA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 57 | `PAYELEMENTSSP600AMT` | DECIMAL(11,4) |  |  |  |  |
| 58 | `PAYELEMENTSAA600DESP` | VARCHAR(200) |  |  |  |  |
| 59 | `PAYELEMENTSAA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 60 | `PAYELEMENTHA600DESP` | VARCHAR(200) |  |  |  |  |
| 61 | `PAYELEMENTHA601DESP` | VARCHAR(200) |  |  |  |  |
| 62 | `PAYELEMENTHA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 63 | `PAYELEMENTHA601AMT` | DECIMAL(11,4) |  |  |  |  |
| 64 | `PAYELEMENTCA600DESP` | VARCHAR(200) |  |  |  |  |
| 65 | `PAYELEMENTCA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 66 | `PAYELEMENTSD600AMT` | DECIMAL(11,4) |  |  |  |  |
| 67 | `PAYELEMENTSD600DESP` | VARCHAR(200) |  |  |  |  |
| 68 | `PAYELEMENTCOM600DESP` | VARCHAR(200) |  |  |  |  |
| 69 | `PAYELEMENTDS600DESP` | VARCHAR(200) |  |  |  |  |
| 70 | `PAYELEMENTCOM600AMT` | DECIMAL(11,4) |  |  |  |  |
| 71 | `PAYELEMENTDS600AMT` | DECIMAL(11,4) |  |  |  |  |
| 72 | `PAYELEMENTSA600DESP` | VARCHAR(200) |  |  |  |  |
| 73 | `PAYELEMENTSA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 74 | `PAYELEMENTMA600DESP` | VARCHAR(200) |  |  |  |  |
| 75 | `PAYELEMENTMBS600DESP` | VARCHAR(200) |  |  |  |  |
| 76 | `PAYELEMENTMA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 77 | `PAYELEMENTMBS600AMT` | DECIMAL(11,4) |  |  |  |  |
| 78 | `PAYELEMENTWA600DESP` | VARCHAR(200) |  |  |  |  |
| 79 | `PAYELEMENTWA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 80 | `PAYELEMENTBA600DESP` | VARCHAR(200) |  |  |  |  |
| 81 | `PAYELEMENTBA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 82 | `PAYELEMENTOA600DESP` | VARCHAR(200) |  |  |  |  |
| 83 | `PAYELEMENTOAE600DESP` | VARCHAR(200) |  |  |  |  |
| 84 | `PAYELEMENTOA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 85 | `PAYELEMENTOAE600AMT` | DECIMAL(11,4) |  |  |  |  |
| 86 | `PAYELEMENTEC600DESP` | VARCHAR(200) |  |  |  |  |
| 87 | `PAYELEMENTEA600DESP` | VARCHAR(200) |  |  |  |  |
| 88 | `PAYELEMENTEC600AMT` | DECIMAL(11,4) |  |  |  |  |
| 89 | `PAYELEMENTEA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 90 | `PAYELEMENTGS600DESP` | VARCHAR(200) |  |  |  |  |
| 91 | `PAYELEMENTGT600DESP` | VARCHAR(200) |  |  |  |  |
| 92 | `PAYELEMENTGW600DESP` | VARCHAR(200) |  |  |  |  |
| 93 | `PAYELEMENTGS600AMT` | DECIMAL(11,4) |  |  |  |  |
| 94 | `PAYELEMENTGT600AMT` | DECIMAL(11,4) |  |  |  |  |
| 95 | `PAYELEMENTGW600AMT` | DECIMAL(11,4) |  |  |  |  |
| 96 | `PAYELEMENTSFA600DESP` | VARCHAR(200) |  |  |  |  |
| 97 | `PAYELEMENTSFA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 98 | `PAYELEMENTETA600DESP` | VARCHAR(200) |  |  |  |  |
| 99 | `PAYELEMENTETA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 100 | `PAYELEMENTPB600DESP` | VARCHAR(200) |  |  |  |  |
| 101 | `PAYELEMENTPB600AMT` | DECIMAL(11,4) |  |  |  |  |
| 102 | `PAYELEMENTLTA600DESP` | VARCHAR(200) |  |  |  |  |
| 103 | `PAYELEMENTLTA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 104 | `PAYELEMENTLC600DESP` | VARCHAR(200) |  |  |  |  |
| 105 | `PAYELEMENTLC600AMT` | DECIMAL(11,4) |  |  |  |  |
| 106 | `PAYELEMENTOI600DESP` | VARCHAR(200) |  |  |  |  |
| 107 | `PAYELEMENTOI600AMT` | DECIMAL(11,4) |  |  |  |  |
| 108 | `PAYELEMENTLW600DESP` | VARCHAR(200) |  |  |  |  |
| 109 | `PAYELEMENTLW600AMT` | DECIMAL(11,4) |  |  |  |  |
| 110 | `PAYELEMENTBE600DESP` | VARCHAR(200) |  |  |  |  |
| 111 | `PAYELEMENTBE600AMT` | DECIMAL(11,4) |  |  |  |  |
| 112 | `PAYELEMENTEX600AMT` | DECIMAL(11,4) |  |  |  |  |
| 113 | `PAYELEMENTEX600DESP` | VARCHAR(200) |  |  |  |  |
| 114 | `PAYELEMENTOT600DESP` | VARCHAR(200) |  |  |  |  |
| 115 | `PAYELEMENTOT600AMT` | DECIMAL(11,4) |  |  |  |  |
| 116 | `PAYELEMENTEI600DESP` | VARCHAR(200) |  |  |  |  |
| 117 | `PAYELEMENTEI600AMT` | DECIMAL(11,4) |  |  |  |  |
| 118 | `PAYELEMENTEL600AMT` | DECIMAL(11,4) |  |  |  |  |
| 119 | `PAYELEMENTAI600DESP` | VARCHAR(200) |  |  |  |  |
| 120 | `PAYELEMENTAIC600DESP` | VARCHAR(200) |  |  |  |  |
| 121 | `PAYELEMENTAI600AMT` | DECIMAL(11,4) |  |  |  |  |
| 122 | `PAYELEMENTAIC600AMT` | DECIMAL(11,4) |  |  |  |  |
| 123 | `PAYELEMENTGI600DESP` | VARCHAR(200) |  |  |  |  |
| 124 | `PAYELEMENTGI600AMT` | DECIMAL(11,4) |  |  |  |  |
| 125 | `PAYELEMENTWOI600DESP` | VARCHAR(200) |  |  |  |  |
| 126 | `PAYELEMENTQUA600DESP` | VARCHAR(200) |  |  |  |  |
| 127 | `PAYELEMENTXYZ600DESP` | VARCHAR(200) |  |  |  |  |
| 128 | `PAYELEMENTWOI600AMT` | DECIMAL(11,4) |  |  |  |  |
| 129 | `PAYELEMENTQUA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 130 | `PAYELEMENTXYZ600AMT` | DECIMAL(11,4) |  |  |  |  |
| 131 | `PAYELEMENTNSI600DESP` | VARCHAR(200) |  |  |  |  |
| 132 | `PAYELEMENTNSI600AMT` | DECIMAL(11,4) |  |  |  |  |
| 133 | `PAYELEMENTWLI600DESP` | VARCHAR(200) |  |  |  |  |
| 134 | `PAYELEMENTWLI600AMT` | DECIMAL(11,4) |  |  |  |  |
| 135 | `PAYELEMENTMR600DESP` | VARCHAR(200) |  |  |  |  |
| 136 | `PAYELEMENTMR600AMT` | DECIMAL(11,4) |  |  |  |  |
| 137 | `PAYELEMENTLTR600DESP` | VARCHAR(200) |  |  |  |  |
| 138 | `PAYELEMENTLTR600AMT` | DECIMAL(11,4) |  |  |  |  |
| 139 | `PAYELEMENTMHR600DESP` | VARCHAR(200) |  |  |  |  |
| 140 | `PAYELEMENTMHR600AMT` | DECIMAL(11,4) |  |  |  |  |
| 141 | `PAYELEMENTPRA600DESP` | VARCHAR(200) |  |  |  |  |
| 142 | `PAYELEMENTPRA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 143 | `PAYELEMENTAB100DESP` | VARCHAR(200) |  |  |  |  |
| 144 | `PAYELEMENTAB100AMT` | DECIMAL(11,4) |  |  |  |  |
| 145 | `PAYELEMENTEL600DESP` | VARCHAR(200) |  |  |  |  |
| 146 | `PAYELEMENTCLB300DESP` | VARCHAR(200) |  |  |  |  |
| 147 | `PAYELEMENTCLB300AMT` | DECIMAL(11,4) |  |  |  |  |
| 148 | `PAYELEMENTFTE600DESP` | VARCHAR(200) |  |  |  |  |
| 149 | `PAYELEMENTFTW600DESP` | VARCHAR(200) |  |  |  |  |
| 150 | `PAYELEMENTFTE600AMT` | DECIMAL(11,4) |  |  |  |  |
| 151 | `PAYELEMENTFTW600AMT` | DECIMAL(11,4) |  |  |  |  |
| 152 | `PAYELEMENTCLN300DESP` | VARCHAR(200) |  |  |  |  |
| 153 | `PAYELEMENTCLN300AMT` | DECIMAL(11,4) |  |  |  |  |
| 154 | `PAYELEMENTCML600AMT` | DECIMAL(11,4) |  |  |  |  |
| 155 | `PAYELEMENTMHA600DESP` | VARCHAR(200) |  |  |  |  |
| 156 | `PAYELEMENTMHA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 157 | `PAYELEMENTCBL300DESP` | VARCHAR(200) |  |  |  |  |
| 158 | `PAYELEMENTCML600DESP` | VARCHAR(200) |  |  |  |  |
| 159 | `PAYELEMENTAFC300DESP` | VARCHAR(200) |  |  |  |  |
| 160 | `PAYELEMENTAFC300AMT` | DECIMAL(11,4) |  |  |  |  |
| 161 | `PAYELEMENTWEA600DESP` | VARCHAR(200) |  |  |  |  |
| 162 | `PAYELEMENTWEA600AMT` | DECIMAL(11,4) |  |  |  |  |
| 163 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 164 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKSALARYWAGEMONTHWISEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.WORKMILLNO,
       t.EMPLOYEECODE,
       t.EMPNAME,
       t.DATEOFJOINING,
       t.DATEOFLEAVING,
       t.GENDER,
       t.SECTION,
       t.GRADE,
       t.DESIGNATION,
       t.COSTCENTERCODE
FROM   DB2ADMIN.WRKSALARYWAGEMONTHWISE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
