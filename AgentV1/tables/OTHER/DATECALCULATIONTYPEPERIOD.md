# DB2ADMIN.DATECALCULATIONTYPEPERIOD

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `DATECALCULATIONTYPECOMPANYCODE`, `DATECALCULATIONTYPECODE`, `PERIODNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 22446

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DATECALCULATIONTYPECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `DATECALCULATIONTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PERIODNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `BASEMONTHDAY` | INTEGER | NOT NULL |  |  |  |
| 4 | `PERIODTYPECODE` | CHAR(10) |  | FK | foreign_key |  |
| 5 | `ADDINGMONTHS` | INTEGER | NOT NULL |  |  |  |
| 6 | `ADDINGDAYS` | INTEGER | NOT NULL |  |  |  |
| 7 | `FIXEDMONTHDAY` | INTEGER | NOT NULL |  |  |  |
| 8 | `FIXEDWEEKDAY` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `COMPETENCEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 10 | `EVENTVLTINFLUENCEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 11 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `DATECALCULATIONTYPEPERIOD.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `DATECALCULATIONTYPE_PERIOD` | `DATECALCULATIONTYPECOMPANYCODE`, `DATECALCULATIONTYPECODE` | [`DATECALCULATIONTYPE`](../OTHER/DATECALCULATIONTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DATECALCULATIONTYPEPERIOD.DATECALCULATIONTYPECOMPANYCODE = DATECALCULATIONTYPE.COMPANYCODE AND DATECALCULATIONTYPEPERIOD.DATECALCULATIONTYPECODE = DATECALCULATIONTYPE.CODE` |
| `PERIODIZEDCALENDARTYPE_PERIODTYPE` | `PERIODTYPECODE` | [`PERIODIZEDCALENDARTYPE`](../CORE_MASTER/PERIODIZEDCALENDARTYPE.md) | `CODE` | RESTRICT | `DATECALCULATIONTYPEPERIOD.PERIODTYPECODE = PERIODIZEDCALENDARTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DATECALCULATIONTYPEPERIODUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DATECALCULATIONTYPECOMPANYCODE,
       t.DATECALCULATIONTYPECODE,
       t.PERIODNUMBER,
       t.BASEMONTHDAY,
       t.PERIODTYPECODE,
       t.ADDINGMONTHS,
       t.ADDINGDAYS,
       t.FIXEDMONTHDAY,
       t.FIXEDWEEKDAY,
       t.COMPETENCEPERCENTAGE,
       t.EVENTVLTINFLUENCEPERCENTAGE,
       t.OWNINGCOMPANYCODE
FROM   DB2ADMIN.DATECALCULATIONTYPEPERIOD t
FETCH FIRST 100 ROWS ONLY;
```
