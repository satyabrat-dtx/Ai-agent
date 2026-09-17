# DB2ADMIN.LUTENTRYLINE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `LUTENTRYCOMPANYCODE`, `LUTENTRYSCHEMETYPECODE`, `LUTENTRYLUTNO`, `COMMERCIALINVOICEDIVISIONCODE`, `COMMERCIALINVOICECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 140152

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LUTENTRYCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `LUTENTRYSCHEMETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LUTENTRYLUTNO` | CHAR(35) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `COMMERCIALINVOICEDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `COMMERCIALINVOICECODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `BENEFITAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 6 | `UPDATEFLAG` | INTEGER | NOT NULL |  |  |  |
| 7 | `TEMPLINEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMMERCIALINVOICE_COMMERCIALINVOICE` | `LUTENTRYCOMPANYCODE`, `COMMERCIALINVOICEDIVISIONCODE`, `COMMERCIALINVOICECODE` | [`COMMERCIALINVOICE`](../CORE_MASTER/COMMERCIALINVOICE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `LUTENTRYLINE.LUTENTRYCOMPANYCODE = COMMERCIALINVOICE.COMPANYCODE AND LUTENTRYLINE.COMMERCIALINVOICEDIVISIONCODE = COMMERCIALINVOICE.DIVISIONCODE AND LUTENTRYLINE.COMMERCIALINVOICECODE = COMMERCIALINVOICE.CODE` |
| `LUTENTRY_LINE` | `LUTENTRYCOMPANYCODE`, `LUTENTRYSCHEMETYPECODE`, `LUTENTRYLUTNO` | [`LUTENTRY`](../OTHER/LUTENTRY.md) | `COMPANYCODE`, `SCHEMETYPECODE`, `LUTNO` | RESTRICT | `LUTENTRYLINE.LUTENTRYCOMPANYCODE = LUTENTRY.COMPANYCODE AND LUTENTRYLINE.LUTENTRYSCHEMETYPECODE = LUTENTRY.SCHEMETYPECODE AND LUTENTRYLINE.LUTENTRYLUTNO = LUTENTRY.LUTNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LUTENTRYLINEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.LUTENTRYCOMPANYCODE,
       t.LUTENTRYSCHEMETYPECODE,
       t.LUTENTRYLUTNO,
       t.COMMERCIALINVOICEDIVISIONCODE,
       t.COMMERCIALINVOICECODE,
       t.BENEFITAMOUNT,
       t.UPDATEFLAG,
       t.TEMPLINEAMOUNT,
       t.ABSUNIQUEID
FROM   DB2ADMIN.LUTENTRYLINE t
FETCH FIRST 100 ROWS ONLY;
```
