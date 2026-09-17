# DB2ADMIN.WRKSALARYVARIANCESHEET

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 116
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `PAYROLLCODE`, `ATTENDANCETYPECODE`, `PROCESSPERIOD`, `DIVISIONCODE`, `FACTORYCODE`, `DEPARTMENTCODE`, `CATEGORYCODE`, `SUBCATEGORYCODE`, `FROMDATE`, `TODATE`, `EMPLOYEECODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 163800

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COMPANYNAME` | VARCHAR(200) |  |  |  |  |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `PAYROLLCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `PAYROLLDESCPRITION` | VARCHAR(200) |  |  |  |  |
| 5 | `ATTENDANCETYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `ATTENDANCETYPEDESC` | VARCHAR(200) |  |  |  |  |
| 7 | `PROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 9 | `DIVISIONDESC` | VARCHAR(200) |  |  |  |  |
| 10 | `FACTORYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 11 | `FACTORYDESC` | VARCHAR(200) |  |  |  |  |
| 12 | `DEPARTMENTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 13 | `DEPARTMENTDESC` | VARCHAR(200) |  |  |  |  |
| 14 | `CATEGORYCODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 15 | `CATEGORYDESC` | VARCHAR(200) |  |  |  |  |
| 16 | `SUBCATEGORYCODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 17 | `SUBCATEGORYDESC` | VARCHAR(200) |  |  |  |  |
| 18 | `FROMDATE` | DATE | NOT NULL | PK | primary_key | Inclusive start of a validity period. |
| 19 | `TODATE` | DATE | NOT NULL | PK | primary_key | End of a validity period. |
| 20 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 21 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 22 | `PAYELEMENT1` | CHAR(6) |  |  |  |  |
| 23 | `PAYELEMENTDESC1` | VARCHAR(80) |  |  |  |  |
| 24 | `AMTCALCULATED1` | DECIMAL(9,2) |  |  |  |  |
| 25 | `PAYELEMENT2` | CHAR(6) |  |  |  |  |
| 26 | `PAYELEMENTDESC2` | VARCHAR(80) |  |  |  |  |
| 27 | `AMTCALCULATED2` | DECIMAL(9,2) |  |  |  |  |
| 28 | `PAYELEMENT3` | CHAR(6) |  |  |  |  |
| 29 | `PAYELEMENTDESC3` | VARCHAR(80) |  |  |  |  |
| 30 | `AMTCALCULATED3` | DECIMAL(9,2) |  |  |  |  |
| 31 | `PAYELEMENT4` | CHAR(6) |  |  |  |  |
| 32 | `PAYELEMENTDESC4` | VARCHAR(80) |  |  |  |  |
| 33 | `AMTCALCULATED4` | DECIMAL(9,2) |  |  |  |  |
| 34 | `PAYELEMENT5` | CHAR(6) |  |  |  |  |
| 35 | `PAYELEMENTDESC5` | VARCHAR(80) |  |  |  |  |
| 36 | `AMTCALCULATED5` | DECIMAL(9,2) |  |  |  |  |
| 37 | `PAYELEMENT6` | CHAR(6) |  |  |  |  |
| 38 | `PAYELEMENTDESC6` | VARCHAR(80) |  |  |  |  |
| 39 | `AMTCALCULATED6` | DECIMAL(9,2) |  |  |  |  |
| 40 | `PAYELEMENT7` | CHAR(6) |  |  |  |  |
| 41 | `PAYELEMENTDESC7` | VARCHAR(80) |  |  |  |  |
| 42 | `AMTCALCULATED7` | DECIMAL(9,2) |  |  |  |  |
| 43 | `PAYELEMENT8` | CHAR(6) |  |  |  |  |
| 44 | `PAYELEMENTDESC8` | VARCHAR(80) |  |  |  |  |
| 45 | `AMTCALCULATED8` | DECIMAL(9,2) |  |  |  |  |
| 46 | `PAYELEMENT9` | CHAR(6) |  |  |  |  |
| 47 | `PAYELEMENTDESC9` | VARCHAR(80) |  |  |  |  |
| 48 | `AMTCALCULATED9` | DECIMAL(9,2) |  |  |  |  |
| 49 | `PAYELEMENT10` | CHAR(6) |  |  |  |  |
| 50 | `PAYELEMENTDESC10` | VARCHAR(80) |  |  |  |  |
| 51 | `AMTCALCULATED10` | DECIMAL(9,2) |  |  |  |  |
| 52 | `PAYELEMENT11` | CHAR(6) |  |  |  |  |
| 53 | `PAYELEMENTDESC11` | VARCHAR(80) |  |  |  |  |
| 54 | `AMTCALCULATED11` | DECIMAL(9,2) |  |  |  |  |
| 55 | `PAYELEMENT12` | CHAR(6) |  |  |  |  |
| 56 | `PAYELEMENTDESC12` | VARCHAR(80) |  |  |  |  |
| 57 | `AMTCALCULATED12` | DECIMAL(9,2) |  |  |  |  |
| 58 | `PAYELEMENT13` | CHAR(6) |  |  |  |  |
| 59 | `PAYELEMENTDESC13` | VARCHAR(80) |  |  |  |  |
| 60 | `AMTCALCULATED13` | DECIMAL(9,2) |  |  |  |  |
| 61 | `PAYELEMENT14` | CHAR(6) |  |  |  |  |
| 62 | `PAYELEMENTDESC14` | VARCHAR(80) |  |  |  |  |
| 63 | `AMTCALCULATED14` | DECIMAL(9,2) |  |  |  |  |
| 64 | `PAYELEMENT15` | CHAR(6) |  |  |  |  |
| 65 | `PAYELEMENTDESC15` | VARCHAR(80) |  |  |  |  |
| 66 | `AMTCALCULATED15` | DECIMAL(9,2) |  |  |  |  |
| 67 | `PAYELEMENT16` | CHAR(6) |  |  |  |  |
| 68 | `PAYELEMENTDESC16` | VARCHAR(80) |  |  |  |  |
| 69 | `AMTCALCULATED16` | DECIMAL(9,2) |  |  |  |  |
| 70 | `PAYELEMENT17` | CHAR(6) |  |  |  |  |
| 71 | `PAYELEMENTDESC17` | VARCHAR(80) |  |  |  |  |
| 72 | `AMTCALCULATED17` | DECIMAL(9,2) |  |  |  |  |
| 73 | `PAYELEMENT18` | CHAR(6) |  |  |  |  |
| 74 | `PAYELEMENTDESC18` | VARCHAR(80) |  |  |  |  |
| 75 | `AMTCALCULATED18` | DECIMAL(9,2) |  |  |  |  |
| 76 | `PAYELEMENT19` | CHAR(6) |  |  |  |  |
| 77 | `PAYELEMENTDESC19` | VARCHAR(80) |  |  |  |  |
| 78 | `AMTCALCULATED19` | DECIMAL(9,2) |  |  |  |  |
| 79 | `PAYELEMENT20` | CHAR(6) |  |  |  |  |
| 80 | `PAYELEMENTDESC20` | VARCHAR(80) |  |  |  |  |
| 81 | `AMTCALCULATED20` | DECIMAL(9,2) |  |  |  |  |
| 82 | `PAYELEMENT21` | CHAR(6) |  |  |  |  |
| 83 | `PAYELEMENTDESC21` | VARCHAR(80) |  |  |  |  |
| 84 | `AMTCALCULATED21` | DECIMAL(9,2) |  |  |  |  |
| 85 | `PAYELEMENT22` | CHAR(6) |  |  |  |  |
| 86 | `PAYELEMENTDESC22` | VARCHAR(80) |  |  |  |  |
| 87 | `AMTCALCULATED22` | DECIMAL(9,2) |  |  |  |  |
| 88 | `PAYELEMENT23` | CHAR(6) |  |  |  |  |
| 89 | `PAYELEMENTDESC23` | VARCHAR(80) |  |  |  |  |
| 90 | `AMTCALCULATED23` | DECIMAL(9,2) |  |  |  |  |
| 91 | `PAYELEMENT24` | CHAR(6) |  |  |  |  |
| 92 | `PAYELEMENTDESC24` | VARCHAR(80) |  |  |  |  |
| 93 | `AMTCALCULATED24` | DECIMAL(9,2) |  |  |  |  |
| 94 | `PAYELEMENT25` | CHAR(6) |  |  |  |  |
| 95 | `PAYELEMENTDESC25` | VARCHAR(80) |  |  |  |  |
| 96 | `AMTCALCULATED25` | DECIMAL(9,2) |  |  |  |  |
| 97 | `PAYELEMENT26` | CHAR(6) |  |  |  |  |
| 98 | `PAYELEMENTDESC26` | VARCHAR(80) |  |  |  |  |
| 99 | `AMTCALCULATED26` | DECIMAL(9,2) |  |  |  |  |
| 100 | `PAYELEMENT27` | CHAR(6) |  |  |  |  |
| 101 | `PAYELEMENTDESC27` | VARCHAR(80) |  |  |  |  |
| 102 | `AMTCALCULATED27` | DECIMAL(9,2) |  |  |  |  |
| 103 | `PAYELEMENT28` | CHAR(6) |  |  |  |  |
| 104 | `PAYELEMENTDESC28` | VARCHAR(80) |  |  |  |  |
| 105 | `AMTCALCULATED28` | DECIMAL(9,2) |  |  |  |  |
| 106 | `PAYELEMENT29` | CHAR(6) |  |  |  |  |
| 107 | `PAYELEMENTDESC29` | VARCHAR(80) |  |  |  |  |
| 108 | `AMTCALCULATED29` | DECIMAL(9,2) |  |  |  |  |
| 109 | `PAYELEMENT30` | CHAR(6) |  |  |  |  |
| 110 | `PAYELEMENTDESC30` | VARCHAR(80) |  |  |  |  |
| 111 | `AMTCALCULATED30` | DECIMAL(9,2) |  |  |  |  |
| 112 | `EMPFATHERNAME` | CHAR(50) |  |  |  |  |
| 113 | `NETPAY` | DECIMAL(9,2) |  |  |  |  |
| 114 | `STDBASIC` | DECIMAL(9,2) |  |  |  |  |
| 115 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKSALARYVARIANCESHEETUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COMPANYNAME,
       t.CREATIONTIMESTAMP,
       t.PAYROLLCODE,
       t.PAYROLLDESCPRITION,
       t.ATTENDANCETYPECODE,
       t.ATTENDANCETYPEDESC,
       t.PROCESSPERIOD,
       t.DIVISIONCODE,
       t.DIVISIONDESC,
       t.FACTORYCODE,
       t.FACTORYDESC
FROM   DB2ADMIN.WRKSALARYVARIANCESHEET t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
