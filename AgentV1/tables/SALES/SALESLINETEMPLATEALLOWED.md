# DB2ADMIN.SALESLINETEMPLATEALLOWED

- **Module**: `SALES` (high confidence — table name starts with 'SALES')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `SALESORDERTEMPLATECOMPANYCODE`, `SALESORDERTEMPLATECODE`, `LINETEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 13159

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESORDERTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SALESORDERTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINETEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DEFAULTLINETEMPLATE` | SMALLINT | NOT NULL |  |  |  |
| 4 | `DISCOUNTLINETEMPLATE` | SMALLINT | NOT NULL |  |  |  |
| 5 | `CHARGELINETEMPLATE` | SMALLINT | NOT NULL |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ADVANCEINVOICELINETEMPLATE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `SALESORDERLINETEMPLATE_LINETEMPLATE` | `SALESORDERTEMPLATECOMPANYCODE`, `LINETEMPLATECODE` | [`SALESORDERLINETEMPLATE`](../SALES/SALESORDERLINETEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESLINETEMPLATEALLOWED.SALESORDERTEMPLATECOMPANYCODE = SALESORDERLINETEMPLATE.COMPANYCODE AND SALESLINETEMPLATEALLOWED.LINETEMPLATECODE = SALESORDERLINETEMPLATE.CODE` |
| `SALESORDERTEMPLATE_LINETEMPLATEALLOWED` | `SALESORDERTEMPLATECOMPANYCODE`, `SALESORDERTEMPLATECODE` | [`SALESORDERTEMPLATE`](../SALES/SALESORDERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESLINETEMPLATEALLOWED.SALESORDERTEMPLATECOMPANYCODE = SALESORDERTEMPLATE.COMPANYCODE AND SALESLINETEMPLATEALLOWED.SALESORDERTEMPLATECODE = SALESORDERTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESLINETEMPLATEALLOWEDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALESORDERTEMPLATECOMPANYCODE,
       t.SALESORDERTEMPLATECODE,
       t.LINETEMPLATECODE,
       t.DEFAULTLINETEMPLATE,
       t.DISCOUNTLINETEMPLATE,
       t.CHARGELINETEMPLATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.SALESLINETEMPLATEALLOWED t
FETCH FIRST 100 ROWS ONLY;
```
