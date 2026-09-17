# DB2ADMIN.FINADVANCEPCUTILIZATION

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `FINADVANCECOMPANYCODE`, `FINADVANCEBUSINESSUNITCODE`, `FINADVANCEADVANCENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 176021

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINADVANCECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINADVANCEBUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINADVANCEADVANCENUMBER` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `BANKREFERENCENO` | CHAR(20) |  |  |  |  |
| 4 | `REFERENCEDATE` | DATE |  |  |  |  |
| 5 | `PCBALANCE` | DECIMAL(18,5) |  |  |  |  |
| 6 | `ADJFORBILL` | DECIMAL(18,5) |  |  |  |  |
| 7 | `PCNOLETTERNO` | CHAR(5) |  | FK | foreign_key |  |
| 8 | `PCGENERALLEDGERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `PCGENERALLEDGERCODE` | CHAR(20) |  | FK | foreign_key |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINADVANCE_PCUTILIZATION` | `FINADVANCECOMPANYCODE`, `FINADVANCEBUSINESSUNITCODE`, `FINADVANCEADVANCENUMBER` | [`FINADVANCE`](../FINANCE/FINADVANCE.md) | `COMPANYCODE`, `BUSINESSUNITCODE`, `ADVANCENUMBER` | RESTRICT | `FINADVANCEPCUTILIZATION.FINADVANCECOMPANYCODE = FINADVANCE.COMPANYCODE AND FINADVANCEPCUTILIZATION.FINADVANCEBUSINESSUNITCODE = FINADVANCE.BUSINESSUNITCODE AND FINADVANCEPCUTILIZATION.FINADVANCEADVANCENUMBER = FINADVANCE.ADVANCENUMBER` |
| `FINPACKINGCREDIT_PCNO` | `FINADVANCECOMPANYCODE`, `PCNOLETTERNO` | [`FINPACKINGCREDIT`](../FINANCE/FINPACKINGCREDIT.md) | `COMPANYCODE`, `LETTERNO` | RESTRICT | `FINADVANCEPCUTILIZATION.FINADVANCECOMPANYCODE = FINPACKINGCREDIT.COMPANYCODE AND FINADVANCEPCUTILIZATION.PCNOLETTERNO = FINPACKINGCREDIT.LETTERNO` |
| `GLMASTER_PCGENERALLEDGER` | `PCGENERALLEDGERCOMPANYCODE`, `PCGENERALLEDGERCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINADVANCEPCUTILIZATION.PCGENERALLEDGERCOMPANYCODE = GLMASTER.COMPANYCODE AND FINADVANCEPCUTILIZATION.PCGENERALLEDGERCODE = GLMASTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINADVANCEPCUTILIZATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINADVANCECOMPANYCODE,
       t.FINADVANCEBUSINESSUNITCODE,
       t.FINADVANCEADVANCENUMBER,
       t.BANKREFERENCENO,
       t.REFERENCEDATE,
       t.PCBALANCE,
       t.ADJFORBILL,
       t.PCNOLETTERNO,
       t.PCGENERALLEDGERCOMPANYCODE,
       t.PCGENERALLEDGERCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.FINADVANCEPCUTILIZATION t
FETCH FIRST 100 ROWS ONLY;
```
