# DB2ADMIN.NETGSTINVOICETAXMAPDETAIL

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `NETGSTINVOICETAXMAPCOMPANYCODE`, `NETGSTINVTAXMAPDIVISIONCODE`, `NETGSTINVOICETAXMAPPOSITION`, `NETGSTINVOICETAXMAPREPORTCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 199608

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NETGSTINVOICETAXMAPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `NETGSTINVTAXMAPDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `NETGSTINVOICETAXMAPPOSITION` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `NETGSTINVOICETAXMAPREPORTCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LINENO` | DECIMAL(18,5) | NOT NULL | PK | primary_key |  |
| 5 | `ITAXCODE` | CHAR(3) |  |  |  |  |
| 6 | `ITAXCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 7 | `EXCLUDEFORPURCHASEINVOICE` | SMALLINT | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `NETGSTINVOICETAXMAP_TAXDETAIL` | `NETGSTINVOICETAXMAPCOMPANYCODE`, `NETGSTINVTAXMAPDIVISIONCODE`, `NETGSTINVOICETAXMAPPOSITION`, `NETGSTINVOICETAXMAPREPORTCODE` | [`NETGSTINVOICETAXMAP`](../LOCALIZATION/NETGSTINVOICETAXMAP.md) | `COMPANYCODE`, `DIVISIONCODE`, `POSITION`, `REPORTCODE` | RESTRICT | `NETGSTINVOICETAXMAPDETAIL.NETGSTINVOICETAXMAPCOMPANYCODE = NETGSTINVOICETAXMAP.COMPANYCODE AND NETGSTINVOICETAXMAPDETAIL.NETGSTINVTAXMAPDIVISIONCODE = NETGSTINVOICETAXMAP.DIVISIONCODE AND NETGSTINVOICETAXMAPDETAIL.NETGSTINVOICETAXMAPPOSITION = NETGSTINVOICETAXMAP.POSITION AND NETGSTINVOICETAXMAPDETAIL.NETGSTINVOICETAXMAPREPORTCODE = NETGSTINVOICETAXMAP.REPORTCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NETGSTINVOICETAXMAPDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.NETGSTINVOICETAXMAPCOMPANYCODE,
       t.NETGSTINVTAXMAPDIVISIONCODE,
       t.NETGSTINVOICETAXMAPPOSITION,
       t.NETGSTINVOICETAXMAPREPORTCODE,
       t.LINENO,
       t.ITAXCODE,
       t.ITAXCATEGORYCODE,
       t.EXCLUDEFORPURCHASEINVOICE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.NETGSTINVOICETAXMAPDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
