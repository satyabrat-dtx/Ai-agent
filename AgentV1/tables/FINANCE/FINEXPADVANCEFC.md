# DB2ADMIN.FINEXPADVANCEFC

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `FINEXPADVANCECOMPANYCODE`, `FINEXPADVANCECODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 176249

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINEXPADVANCECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINEXPADVANCECODE` | CHAR(5) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `ADVANCENO` | CHAR(5) |  |  |  |  |
| 4 | `BANKREFNO` | CHAR(20) |  |  |  |  |
| 5 | `DUEDATE` | DATE |  |  |  |  |
| 6 | `RATE` | DECIMAL(18,5) |  |  |  |  |
| 7 | `FCUNUTILISED` | DECIMAL(18,5) |  |  |  |  |
| 8 | `ADJUSTBILL` | DECIMAL(18,5) |  |  |  |  |
| 9 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `FCAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `FCNO` | CHAR(10) |  |  |  |  |
| 12 | `MARKETRATE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `BANKCHARGESUSD` | DECIMAL(18,5) |  |  |  |  |
| 14 | `INRVALUE` | DECIMAL(18,5) |  |  |  |  |
| 15 | `TOTALUSD` | DECIMAL(18,5) |  |  |  |  |
| 16 | `TOTALINR` | DECIMAL(18,5) |  |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINEXPADVANCE_FC` | `FINEXPADVANCECOMPANYCODE`, `FINEXPADVANCECODE` | [`FINEXPADVANCE`](../FINANCE/FINEXPADVANCE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEXPADVANCEFC.FINEXPADVANCECOMPANYCODE = FINEXPADVANCE.COMPANYCODE AND FINEXPADVANCEFC.FINEXPADVANCECODE = FINEXPADVANCE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINEXPADVANCEFCUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINEXPADVANCECOMPANYCODE,
       t.FINEXPADVANCECODE,
       t.LINENO,
       t.ADVANCENO,
       t.BANKREFNO,
       t.DUEDATE,
       t.RATE,
       t.FCUNUTILISED,
       t.ADJUSTBILL,
       t.AMOUNT,
       t.FCAMOUNT,
       t.FCNO
FROM   DB2ADMIN.FINEXPADVANCEFC t
FETCH FIRST 100 ROWS ONLY;
```
