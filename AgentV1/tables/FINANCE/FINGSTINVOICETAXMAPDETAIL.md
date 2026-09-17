# DB2ADMIN.FINGSTINVOICETAXMAPDETAIL

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `FINGSTINVOICETAXMAPCOMPANYCODE`, `FINGSTINVOICETAXMAPDIVISIONCOD`, `FINGSTINVOICETAXMAPPOSITION`, `FINGSTINVOICETAXMAPREPORTCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 180121

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINGSTINVOICETAXMAPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINGSTINVOICETAXMAPDIVISIONCOD` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINGSTINVOICETAXMAPPOSITION` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FINGSTINVOICETAXMAPREPORTCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LINENO` | DECIMAL(18,5) | NOT NULL | PK | primary_key |  |
| 5 | `ITAXCODE` | CHAR(3) |  |  |  |  |
| 6 | `ITAXCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `EXCLUDEFORPURCHASEINVOICE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINGSTINVOICETAXMAP_TAXDETAIL` | `FINGSTINVOICETAXMAPCOMPANYCODE`, `FINGSTINVOICETAXMAPDIVISIONCOD`, `FINGSTINVOICETAXMAPPOSITION`, `FINGSTINVOICETAXMAPREPORTCODE` | [`FINGSTINVOICETAXMAP`](../FINANCE/FINGSTINVOICETAXMAP.md) | `COMPANYCODE`, `DIVISIONCODE`, `POSITION`, `REPORTCODE` | RESTRICT | `FINGSTINVOICETAXMAPDETAIL.FINGSTINVOICETAXMAPCOMPANYCODE = FINGSTINVOICETAXMAP.COMPANYCODE AND FINGSTINVOICETAXMAPDETAIL.FINGSTINVOICETAXMAPDIVISIONCOD = FINGSTINVOICETAXMAP.DIVISIONCODE AND FINGSTINVOICETAXMAPDETAIL.FINGSTINVOICETAXMAPPOSITION = FINGSTINVOICETAXMAP.POSITION AND FINGSTINVOICETAXMAPDETAIL.FINGSTINVOICETAXMAPREPORTCODE = FINGSTINVOICETAXMAP.REPORTCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINGSTINVOICETAXMAPDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINGSTINVOICETAXMAPCOMPANYCODE,
       t.FINGSTINVOICETAXMAPDIVISIONCOD,
       t.FINGSTINVOICETAXMAPPOSITION,
       t.FINGSTINVOICETAXMAPREPORTCODE,
       t.LINENO,
       t.ITAXCODE,
       t.ITAXCATEGORYCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.FINGSTINVOICETAXMAPDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
