# DB2ADMIN.TAXNATURE

- **Module**: `EINVOICING` (low confidence — FK neighbourhood: 3 of 3 related tables are EINVOICING)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `CODE`
- **FK degree**: referenced by 4 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 237603

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(4) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `REVERSECHARGE` | SMALLINT | NOT NULL |  |  |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TAXNATURE_TAXNATURE` | [`TAX`](../CORE_MASTER/TAX.md) | `TAXNATURECODE` | `TAX.TAXNATURECODE = TAXNATURE.CODE` |
| `TAXNATURE_TAXNATURE` | [`EINVOICEGOODSSERVICESDATA`](../EINVOICING/EINVOICEGOODSSERVICESDATA.md) | `TAXNATURECODE` | `EINVOICEGOODSSERVICESDATA.TAXNATURECODE = TAXNATURE.CODE` |
| `TAXNATURE_TAXNATURE` | [`EINVOICEOTHERDATA`](../EINVOICING/EINVOICEOTHERDATA.md) | `TAXNATURECODE` | `EINVOICEOTHERDATA.TAXNATURECODE = TAXNATURE.CODE` |
| `TAXNATURE_TAXNATURE` | [`EINVOICEWALFAREFUNDDATA`](../EINVOICING/EINVOICEWALFAREFUNDDATA.md) | `TAXNATURECODE` | `EINVOICEWALFAREFUNDDATA.TAXNATURECODE = TAXNATURE.CODE` |

## Indexes

- `TAXNATUREUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.REVERSECHARGE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TAXNATURE t
FETCH FIRST 100 ROWS ONLY;
```
