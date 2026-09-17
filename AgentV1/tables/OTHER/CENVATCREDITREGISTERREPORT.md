# DB2ADMIN.CENVATCREDITREGISTERREPORT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 76
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `RG23IICODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE`, `LINENO`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 135307

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `ITAX0CODE` | CHAR(15) |  |  |  |  |
| 3 | `ITAX1CODE` | CHAR(15) |  |  |  |  |
| 4 | `ITAX2CODE` | CHAR(15) |  |  |  |  |
| 5 | `ITAX3CODE` | CHAR(15) |  |  |  |  |
| 6 | `ITAX4CODE` | CHAR(15) |  |  |  |  |
| 7 | `ITAX5CODE` | CHAR(15) |  |  |  |  |
| 8 | `ITAX6CODE` | CHAR(15) |  |  |  |  |
| 9 | `ITAX7CODE` | CHAR(15) |  |  |  |  |
| 10 | `ITAX8CODE` | CHAR(15) |  |  |  |  |
| 11 | `ITAX9CODE` | CHAR(15) |  |  |  |  |
| 12 | `AMOUNT0` | DECIMAL(18,5) |  |  |  |  |
| 13 | `AMOUNT1` | DECIMAL(18,5) |  |  |  |  |
| 14 | `AMOUNT2` | DECIMAL(18,5) |  |  |  |  |
| 15 | `AMOUNT3` | DECIMAL(18,5) |  |  |  |  |
| 16 | `AMOUNT4` | DECIMAL(18,5) |  |  |  |  |
| 17 | `AMOUNT5` | DECIMAL(18,5) |  |  |  |  |
| 18 | `AMOUNT6` | DECIMAL(18,5) |  |  |  |  |
| 19 | `AMOUNT7` | DECIMAL(18,5) |  |  |  |  |
| 20 | `AMOUNT8` | DECIMAL(18,5) |  |  |  |  |
| 21 | `AMOUNT9` | DECIMAL(18,5) |  |  |  |  |
| 22 | `RG23II` | INTEGER | NOT NULL |  |  |  |
| 23 | `CREDIT0` | DECIMAL(18,5) |  |  |  |  |
| 24 | `CREDIT1` | DECIMAL(18,5) |  |  |  |  |
| 25 | `CREDIT2` | DECIMAL(18,5) |  |  |  |  |
| 26 | `CREDIT3` | DECIMAL(18,5) |  |  |  |  |
| 27 | `CREDIT4` | DECIMAL(18,5) |  |  |  |  |
| 28 | `CREDIT5` | DECIMAL(18,5) |  |  |  |  |
| 29 | `CREDIT6` | DECIMAL(18,5) |  |  |  |  |
| 30 | `CREDIT7` | DECIMAL(18,5) |  |  |  |  |
| 31 | `CREDIT8` | DECIMAL(18,5) |  |  |  |  |
| 32 | `CREDIT9` | DECIMAL(18,5) |  |  |  |  |
| 33 | `DEBIT0` | DECIMAL(18,5) |  |  |  |  |
| 34 | `DEBIT1` | DECIMAL(18,5) |  |  |  |  |
| 35 | `DEBIT2` | DECIMAL(18,5) |  |  |  |  |
| 36 | `DEBIT3` | DECIMAL(18,5) |  |  |  |  |
| 37 | `DEBIT4` | DECIMAL(18,5) |  |  |  |  |
| 38 | `DEBIT5` | DECIMAL(18,5) |  |  |  |  |
| 39 | `DEBIT6` | DECIMAL(18,5) |  |  |  |  |
| 40 | `DEBIT7` | DECIMAL(18,5) |  |  |  |  |
| 41 | `DEBIT8` | DECIMAL(18,5) |  |  |  |  |
| 42 | `DEBIT9` | DECIMAL(18,5) |  |  |  |  |
| 43 | `CREDITAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 44 | `DEBITAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 45 | `RG23IICODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 46 | `EXCISEYEARREGNO` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 47 | `EXCISEYEARCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 48 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 49 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 50 | `UPTODATE` | DATE |  |  |  |  |
| 51 | `REPORTFROM` | DATE |  |  |  |  |
| 52 | `REPORTTO` | DATE |  |  |  |  |
| 53 | `INVOICENO` | CHAR(15) |  |  |  |  |
| 54 | `MRNCODE` | DECIMAL(11,0) |  |  |  |  |
| 55 | `INVOICEDATE` | DATE |  |  |  |  |
| 56 | `ITAXFLAG0` | CHAR(1) |  |  |  |  |
| 57 | `ITAXFLAG1` | CHAR(1) |  |  |  |  |
| 58 | `ITAXFLAG2` | CHAR(1) |  |  |  |  |
| 59 | `ITAXFLAG3` | CHAR(1) |  |  |  |  |
| 60 | `ITAXFLAG4` | CHAR(1) |  |  |  |  |
| 61 | `ITAXFLAG5` | CHAR(1) |  |  |  |  |
| 62 | `ITAXFLAG6` | CHAR(1) |  |  |  |  |
| 63 | `ITAXFLAG7` | CHAR(1) |  |  |  |  |
| 64 | `ITAXFLAG8` | CHAR(1) |  |  |  |  |
| 65 | `ITAXFLAG9` | CHAR(1) |  |  |  |  |
| 66 | `PLANTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 67 | `PLANTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 68 | `REMARKS` | CHAR(100) |  |  |  |  |
| 69 | `RG23ICODE` | CHAR(15) |  |  |  |  |
| 70 | `STEP` | CHAR(1) |  |  |  |  |
| 71 | `RANGECODE` | CHAR(15) |  |  |  |  |
| 72 | `RANGEDIVISIONCODE` | CHAR(15) |  |  |  |  |
| 73 | `RANGEDIVISIONDESCRIPTION` | CHAR(100) |  |  |  |  |
| 74 | `ECCNO` | CHAR(30) |  |  |  |  |
| 75 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `CENVATCREDITREGISTERREPORT.COMPANYCODE = COMPANY.CODE` |
| `EXCISEYEAR_EXCISEYEAR` | `COMPANYCODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE` | [`EXCISEYEAR`](../SALES/EXCISEYEAR.md) | `COMPANYCODE`, `REGNO`, `CODE` | RESTRICT | `CENVATCREDITREGISTERREPORT.COMPANYCODE = EXCISEYEAR.COMPANYCODE AND CENVATCREDITREGISTERREPORT.EXCISEYEARREGNO = EXCISEYEAR.REGNO AND CENVATCREDITREGISTERREPORT.EXCISEYEARCODE = EXCISEYEAR.CODE` |
| `PLANT_PLANT` | `PLANTCOMPANYCODE`, `PLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CENVATCREDITREGISTERREPORT.PLANTCOMPANYCODE = PLANT.COMPANYCODE AND CENVATCREDITREGISTERREPORT.PLANTCODE = PLANT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CENVATCREDITREGISTERREPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ITAX0CODE,
       t.ITAX1CODE,
       t.ITAX2CODE,
       t.ITAX3CODE,
       t.ITAX4CODE,
       t.ITAX5CODE,
       t.ITAX6CODE,
       t.ITAX7CODE,
       t.ITAX8CODE,
       t.ITAX9CODE
FROM   DB2ADMIN.CENVATCREDITREGISTERREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
