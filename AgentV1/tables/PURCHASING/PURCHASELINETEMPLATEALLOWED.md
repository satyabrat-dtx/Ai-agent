# DB2ADMIN.PURCHASELINETEMPLATEALLOWED

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `PURORDERTEMPLATECOMPANYCODE`, `PURCHASEORDERTEMPLATECODE`, `LINETEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 3768

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURORDERTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PURCHASEORDERTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
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

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PURCHASEORDERLINETEMPLATE_LINETEMPLATE` | `PURORDERTEMPLATECOMPANYCODE`, `LINETEMPLATECODE` | [`PURCHASEORDERLINETEMPLATE`](../PURCHASING/PURCHASEORDERLINETEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASELINETEMPLATEALLOWED.PURORDERTEMPLATECOMPANYCODE = PURCHASEORDERLINETEMPLATE.COMPANYCODE AND PURCHASELINETEMPLATEALLOWED.LINETEMPLATECODE = PURCHASEORDERLINETEMPLATE.CODE` |
| `PURCHASEORDERTEMPLATE_LINETEMPLATEALLOWED` | `PURORDERTEMPLATECOMPANYCODE`, `PURCHASEORDERTEMPLATECODE` | [`PURCHASEORDERTEMPLATE`](../PURCHASING/PURCHASEORDERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASELINETEMPLATEALLOWED.PURORDERTEMPLATECOMPANYCODE = PURCHASEORDERTEMPLATE.COMPANYCODE AND PURCHASELINETEMPLATEALLOWED.PURCHASEORDERTEMPLATECODE = PURCHASEORDERTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURLINETEMPLATEALLOWEDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PURORDERTEMPLATECOMPANYCODE,
       t.PURCHASEORDERTEMPLATECODE,
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
FROM   DB2ADMIN.PURCHASELINETEMPLATEALLOWED t
FETCH FIRST 100 ROWS ONLY;
```
