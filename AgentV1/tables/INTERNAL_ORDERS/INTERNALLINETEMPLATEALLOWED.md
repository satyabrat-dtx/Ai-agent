# DB2ADMIN.INTERNALLINETEMPLATEALLOWED

- **Module**: `INTERNAL_ORDERS` (high confidence — table name starts with 'INTERNAL')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `INTORDERTEMPLATECOMPANYCODE`, `INTERNALORDERTEMPLATECODE`, `LINETEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 20738

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INTORDERTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `INTERNALORDERTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINETEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DEFAULTLINETEMPLATE` | SMALLINT | NOT NULL |  |  |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `INTERNALORDERLINETEMPLATE_LINETEMPLATE` | `INTORDERTEMPLATECOMPANYCODE`, `LINETEMPLATECODE` | [`INTERNALORDERLINETEMPLATE`](../INTERNAL_ORDERS/INTERNALORDERLINETEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INTERNALLINETEMPLATEALLOWED.INTORDERTEMPLATECOMPANYCODE = INTERNALORDERLINETEMPLATE.COMPANYCODE AND INTERNALLINETEMPLATEALLOWED.LINETEMPLATECODE = INTERNALORDERLINETEMPLATE.CODE` |
| `INTERNALORDERTEMPLATE_LINETEMPLATEALLOWED` | `INTORDERTEMPLATECOMPANYCODE`, `INTERNALORDERTEMPLATECODE` | [`INTERNALORDERTEMPLATE`](../INTERNAL_ORDERS/INTERNALORDERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INTERNALLINETEMPLATEALLOWED.INTORDERTEMPLATECOMPANYCODE = INTERNALORDERTEMPLATE.COMPANYCODE AND INTERNALLINETEMPLATEALLOWED.INTERNALORDERTEMPLATECODE = INTERNALORDERTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INTLINETEMPLATEALLOWEDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.INTORDERTEMPLATECOMPANYCODE,
       t.INTERNALORDERTEMPLATECODE,
       t.LINETEMPLATECODE,
       t.DEFAULTLINETEMPLATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.INTERNALLINETEMPLATEALLOWED t
FETCH FIRST 100 ROWS ONLY;
```
