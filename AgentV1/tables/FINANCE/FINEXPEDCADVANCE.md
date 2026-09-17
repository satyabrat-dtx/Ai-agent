# DB2ADMIN.FINEXPEDCADVANCE

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `FINEXPEDCHARGESCOMPANYCODE`, `FINEXPEDCHARGESCODE`, `ADVANCECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 176352

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINEXPEDCHARGESCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINEXPEDCHARGESCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ADVANCECODE` | CHAR(5) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `REFERENCENUM` | CHAR(15) |  |  |  |  |
| 4 | `REFERENCEDATE` | DATE |  |  |  |  |
| 5 | `ADJUSTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 6 | `RATEDIFF` | DECIMAL(18,5) |  |  |  |  |
| 7 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `BANKCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 9 | `POSTED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINEXPADVANCE_ADVANCE` | `FINEXPEDCHARGESCOMPANYCODE`, `ADVANCECODE` | [`FINEXPADVANCE`](../FINANCE/FINEXPADVANCE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEXPEDCADVANCE.FINEXPEDCHARGESCOMPANYCODE = FINEXPADVANCE.COMPANYCODE AND FINEXPEDCADVANCE.ADVANCECODE = FINEXPADVANCE.CODE` |
| `FINEXPEDCHARGES_ADVANCE` | `FINEXPEDCHARGESCOMPANYCODE`, `FINEXPEDCHARGESCODE` | [`FINEXPEDCHARGES`](../FINANCE/FINEXPEDCHARGES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEXPEDCADVANCE.FINEXPEDCHARGESCOMPANYCODE = FINEXPEDCHARGES.COMPANYCODE AND FINEXPEDCADVANCE.FINEXPEDCHARGESCODE = FINEXPEDCHARGES.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINEXPEDCADVANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINEXPEDCHARGESCOMPANYCODE,
       t.FINEXPEDCHARGESCODE,
       t.ADVANCECODE,
       t.REFERENCENUM,
       t.REFERENCEDATE,
       t.ADJUSTEDAMOUNT,
       t.RATEDIFF,
       t.VALUE,
       t.BANKCHARGES,
       t.POSTED,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.FINEXPEDCADVANCE t
FETCH FIRST 100 ROWS ONLY;
```
