# DB2ADMIN.FINADVANCEFCUTILIZATION

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `FINADVANCECOMPANYCODE`, `FINADVANCEBUSINESSUNITCODE`, `FINADVANCEADVANCENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 175969

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINADVANCECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINADVANCEBUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINADVANCEADVANCENUMBER` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `BANKREFERENCENO` | CHAR(20) |  |  |  |  |
| 4 | `DUEDATE` | DATE |  |  |  |  |
| 5 | `RATE` | DECIMAL(18,5) |  |  |  |  |
| 6 | `UNUTILISED` | DECIMAL(18,5) |  |  |  |  |
| 7 | `ADJFORBILL` | DECIMAL(18,5) |  |  |  |  |
| 8 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `FCNOFCNO` | CHAR(10) |  | FK | foreign_key |  |
| 10 | `MARKETRATE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `BANKCHARGESUSD` | DECIMAL(18,5) |  |  |  |  |
| 12 | `INRVALUEFIELD` | DECIMAL(18,5) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `FINADVFCUTILOGMGMNT` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINADVANCE_FCUTILIZATION` | `FINADVANCECOMPANYCODE`, `FINADVANCEBUSINESSUNITCODE`, `FINADVANCEADVANCENUMBER` | [`FINADVANCE`](../FINANCE/FINADVANCE.md) | `COMPANYCODE`, `BUSINESSUNITCODE`, `ADVANCENUMBER` | RESTRICT | `FINADVANCEFCUTILIZATION.FINADVANCECOMPANYCODE = FINADVANCE.COMPANYCODE AND FINADVANCEFCUTILIZATION.FINADVANCEBUSINESSUNITCODE = FINADVANCE.BUSINESSUNITCODE AND FINADVANCEFCUTILIZATION.FINADVANCEADVANCENUMBER = FINADVANCE.ADVANCENUMBER` |
| `FINFORWARDCONTRACT_FCNO` | `FINADVANCECOMPANYCODE`, `FCNOFCNO` | [`FINFORWARDCONTRACT`](../FINANCE/FINFORWARDCONTRACT.md) | `COMPANYCODE`, `FCNO` | RESTRICT | `FINADVANCEFCUTILIZATION.FINADVANCECOMPANYCODE = FINFORWARDCONTRACT.COMPANYCODE AND FINADVANCEFCUTILIZATION.FCNOFCNO = FINFORWARDCONTRACT.FCNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINADVANCEFCUTILIZATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINADVANCECOMPANYCODE,
       t.FINADVANCEBUSINESSUNITCODE,
       t.FINADVANCEADVANCENUMBER,
       t.BANKREFERENCENO,
       t.DUEDATE,
       t.RATE,
       t.UNUTILISED,
       t.ADJFORBILL,
       t.AMOUNT,
       t.FCNOFCNO,
       t.MARKETRATE,
       t.BANKCHARGESUSD
FROM   DB2ADMIN.FINADVANCEFCUTILIZATION t
FETCH FIRST 100 ROWS ONLY;
```
