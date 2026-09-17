# DB2ADMIN.PAYTEMPLATEDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `PAYTEMPLATECOMPANYCODE`, `PAYTEMPLATECODE`, `PAYELEMENTTYPE`, `PAYELEMENTCODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 155538

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PAYTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PAYTEMPLATECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PAYELEMENTTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PAYELEMENTCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 5 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 6 | `FORMULAFLAG` | INTEGER | NOT NULL |  |  |  |
| 7 | `ELIGIBILITYCODE` | CHAR(6) |  | FK | foreign_key |  |
| 8 | `FORMULACODE` | CHAR(6) |  | FK | foreign_key |  |
| 9 | `LUMPSUMVALUE` | DECIMAL(9,2) |  |  |  |  |
| 10 | `PRIORITYNO` | DECIMAL(5,0) |  |  |  |  |
| 11 | `FLAGCARRYFORWARD` | INTEGER | NOT NULL |  |  |  |
| 12 | `FLAGPARTIALCARRYFORWARD` | INTEGER | NOT NULL |  |  |  |
| 13 | `FLAGREGPAYROLL` | INTEGER | NOT NULL |  |  |  |
| 14 | `FLAGHOLIDAYPAYROLL` | INTEGER | NOT NULL |  |  |  |
| 15 | `FLAGREGOTPAYROLL` | INTEGER | NOT NULL |  |  |  |
| 16 | `FLAGWOFFPAYROLL` | INTEGER | NOT NULL |  |  |  |
| 17 | `FLAGHOLIDAYOTPAYROLL` | INTEGER | NOT NULL |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `FLAGWOFFOTPAYROLL` | INTEGER | NOT NULL |  |  |  |
| 25 | `TAXAPPLICABLEMONTH` | SMALLINT | NOT NULL |  |  |  |
| 26 | `STEP` | CHAR(1) |  |  |  |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FORMULACODE_FORMULA` | `PAYTEMPLATECOMPANYCODE`, `FORMULACODE` | [`FORMULACODE`](../HR/FORMULACODE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PAYTEMPLATEDETAIL.PAYTEMPLATECOMPANYCODE = FORMULACODE.COMPANYCODE AND PAYTEMPLATEDETAIL.FORMULACODE = FORMULACODE.CODE` |
| `PAYELEMENT_PAYELEMENT` | `PAYTEMPLATECOMPANYCODE`, `PAYELEMENTTYPE`, `PAYELEMENTCODE` | [`PAYELEMENT`](../CORE_MASTER/PAYELEMENT.md) | `COMPANYCODE`, `PAYELEMENTTYPE`, `CODE` | RESTRICT | `PAYTEMPLATEDETAIL.PAYTEMPLATECOMPANYCODE = PAYELEMENT.COMPANYCODE AND PAYTEMPLATEDETAIL.PAYELEMENTTYPE = PAYELEMENT.PAYELEMENTTYPE AND PAYTEMPLATEDETAIL.PAYELEMENTCODE = PAYELEMENT.CODE` |
| `PAYTEMPLATE_LINE` | `PAYTEMPLATECOMPANYCODE`, `PAYTEMPLATECODE` | [`PAYTEMPLATE`](../HR/PAYTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PAYTEMPLATEDETAIL.PAYTEMPLATECOMPANYCODE = PAYTEMPLATE.COMPANYCODE AND PAYTEMPLATEDETAIL.PAYTEMPLATECODE = PAYTEMPLATE.CODE` |
| `USERELIGIBILITY_ELIGIBILITY` | `PAYTEMPLATECOMPANYCODE`, `ELIGIBILITYCODE` | [`USERELIGIBILITY`](../HR/USERELIGIBILITY.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PAYTEMPLATEDETAIL.PAYTEMPLATECOMPANYCODE = USERELIGIBILITY.COMPANYCODE AND PAYTEMPLATEDETAIL.ELIGIBILITYCODE = USERELIGIBILITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PAYTEMPLATEDETAILUID` (ABSUNIQUEID)
- `INDCUST1` (PAYTEMPLATECOMPANYCODE, PAYTEMPLATECODE, EFFECTIVEFROMDATE, EFFECTIVETODATE)

## Starter query

```sql
SELECT t.PAYTEMPLATECOMPANYCODE,
       t.PAYTEMPLATECODE,
       t.PAYELEMENTTYPE,
       t.PAYELEMENTCODE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.FORMULAFLAG,
       t.ELIGIBILITYCODE,
       t.FORMULACODE,
       t.LUMPSUMVALUE,
       t.PRIORITYNO,
       t.FLAGCARRYFORWARD
FROM   DB2ADMIN.PAYTEMPLATEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
