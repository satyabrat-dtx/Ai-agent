# DB2ADMIN.BARCODETYPE

- **Module**: `CORE_MASTER` (low confidence — referenced across 4 modules, so shared reference data)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `CODE`
- **FK degree**: referenced by 9 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 11622

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(2) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `BARCODEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 5 | `FONT` | CHAR(30) |  |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `FORMAT` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 9

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `BARCODETYPE_BARTYPE` | [`ORDERITEMORDERPARTNERLINK`](../OTHER/ORDERITEMORDERPARTNERLINK.md) | `BARTYPECODE` | `ORDERITEMORDERPARTNERLINK.BARTYPECODE = BARCODETYPE.CODE` |
| `BARCODETYPE_BARTYPE` | [`NONINVENTORY`](../INTRASTAT/NONINVENTORY.md) | `BARTYPECODE` | `NONINVENTORY.BARTYPECODE = BARCODETYPE.CODE` |
| `BARCODETYPE_BARTYPE` | [`TOOL`](../CORE_MASTER/TOOL.md) | `BARTYPECODE` | `TOOL.BARTYPECODE = BARCODETYPE.CODE` |
| `BARCODETYPE_BARTYPE` | [`PRODUCT`](../ITEM_MASTER/PRODUCT.md) | `BARTYPECODE` | `PRODUCT.BARTYPECODE = BARCODETYPE.CODE` |
| `BARCODETYPE_BARTYPE` | [`PDMARB0`](../PDM/PDMARB0.md) | `BARTYPECODE` | `PDMARB0.BARTYPECODE = BARCODETYPE.CODE` |
| `BARCODETYPE_BARTYPE` | [`FULLITEMKEYDECODER`](../COSTING/FULLITEMKEYDECODER.md) | `BARTYPECODE` | `FULLITEMKEYDECODER.BARTYPECODE = BARCODETYPE.CODE` |
| `BARCODETYPE_BARTYPE` | [`SELLINGITEM`](../OTHER/SELLINGITEM.md) | `BARTYPECODE` | `SELLINGITEM.BARTYPECODE = BARCODETYPE.CODE` |
| `BARCODETYPE_BARTYPE` | [`CONTAINER`](../CORE_MASTER/CONTAINER.md) | `BARTYPECODE` | `CONTAINER.BARTYPECODE = BARCODETYPE.CODE` |
| `BARCODETYPE_BARTYPE` | [`DEVELOPMENTREQUESTDETAIL`](../CORE_MASTER/DEVELOPMENTREQUESTDETAIL.md) | `BARTYPECODE` | `DEVELOPMENTREQUESTDETAIL.BARTYPECODE = BARCODETYPE.CODE` |

## Indexes

- `BARCODETYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.BARCODEPOLICYCODE,
       t.FONT,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.BARCODETYPE t
FETCH FIRST 100 ROWS ONLY;
```
