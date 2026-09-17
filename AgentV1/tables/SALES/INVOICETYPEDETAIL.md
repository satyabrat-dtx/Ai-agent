# DB2ADMIN.INVOICETYPEDETAIL

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `INVOICETYPECOMPANYCODE`, `INVOICETYPEDIVISIONCODE`, `INVOICETYPECODE`, `ALLOWEDINVOICETYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 124662

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INVOICETYPECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `INVOICETYPEDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INVOICETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ALLOWEDINVOICETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `INVOICETYPE_ALLOWEDINVOICETYPE` | `INVOICETYPECOMPANYCODE`, `INVOICETYPEDIVISIONCODE`, `ALLOWEDINVOICETYPECODE` | [`INVOICETYPE`](../SALES/INVOICETYPE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `INVOICETYPEDETAIL.INVOICETYPECOMPANYCODE = INVOICETYPE.COMPANYCODE AND INVOICETYPEDETAIL.INVOICETYPEDIVISIONCODE = INVOICETYPE.DIVISIONCODE AND INVOICETYPEDETAIL.ALLOWEDINVOICETYPECODE = INVOICETYPE.CODE` |
| `INVOICETYPE_DETAIL` | `INVOICETYPECOMPANYCODE`, `INVOICETYPEDIVISIONCODE`, `INVOICETYPECODE` | [`INVOICETYPE`](../SALES/INVOICETYPE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `INVOICETYPEDETAIL.INVOICETYPECOMPANYCODE = INVOICETYPE.COMPANYCODE AND INVOICETYPEDETAIL.INVOICETYPEDIVISIONCODE = INVOICETYPE.DIVISIONCODE AND INVOICETYPEDETAIL.INVOICETYPECODE = INVOICETYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INVOICETYPEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.INVOICETYPECOMPANYCODE,
       t.INVOICETYPEDIVISIONCODE,
       t.INVOICETYPECODE,
       t.ALLOWEDINVOICETYPECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.INVOICETYPEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
