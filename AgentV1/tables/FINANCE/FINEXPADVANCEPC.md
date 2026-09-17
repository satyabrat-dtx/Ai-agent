# DB2ADMIN.FINEXPADVANCEPC

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `FINEXPADVANCECOMPANYCODE`, `FINEXPADVANCECODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 176304

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINEXPADVANCECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINEXPADVANCECODE` | CHAR(5) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `ADVANCENO` | CHAR(5) |  |  |  |  |
| 4 | `BANKREFNO` | CHAR(30) |  |  |  |  |
| 5 | `REFDATE` | DATE |  |  |  |  |
| 6 | `PCBALANCE` | DECIMAL(18,5) |  |  |  |  |
| 7 | `ADJUSTBILL` | DECIMAL(18,5) |  |  |  |  |
| 8 | `PCNO` | CHAR(20) |  |  |  |  |
| 9 | `PCGENERALLEDGER` | CHAR(20) |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINEXPADVANCE_PC` | `FINEXPADVANCECOMPANYCODE`, `FINEXPADVANCECODE` | [`FINEXPADVANCE`](../FINANCE/FINEXPADVANCE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEXPADVANCEPC.FINEXPADVANCECOMPANYCODE = FINEXPADVANCE.COMPANYCODE AND FINEXPADVANCEPC.FINEXPADVANCECODE = FINEXPADVANCE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINEXPADVANCEPCUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINEXPADVANCECOMPANYCODE,
       t.FINEXPADVANCECODE,
       t.LINENO,
       t.ADVANCENO,
       t.BANKREFNO,
       t.REFDATE,
       t.PCBALANCE,
       t.ADJUSTBILL,
       t.PCNO,
       t.PCGENERALLEDGER,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.FINEXPADVANCEPC t
FETCH FIRST 100 ROWS ONLY;
```
