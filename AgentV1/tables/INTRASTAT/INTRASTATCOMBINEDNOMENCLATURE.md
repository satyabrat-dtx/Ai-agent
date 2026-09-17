# DB2ADMIN.INTRASTATCOMBINEDNOMENCLATURE

- **Module**: `INTRASTAT` (high confidence — table name starts with 'INTRASTAT')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `CODE`
- **FK degree**: referenced by 8 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 31224

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(11) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `EXCLUDEDINTEREEC` | SMALLINT | NOT NULL |  |  |  |
| 5 | `SUPPLUMREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `SUPPLEMENTARYUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `INTRASTATTRNLINEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `UNITOFMEASURE_SUPPLEMENTARYUM` | `SUPPLEMENTARYUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `INTRASTATCOMBINEDNOMENCLATURE.SUPPLEMENTARYUMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 8

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `INTRASTATCOMBINEDNOMENCLATURE_NOMENCLATUREINTRACEE` | [`INTRASTATTRANSACTIONS`](../INTRASTAT/INTRASTATTRANSACTIONS.md) | `NOMENCLATUREINTRACEECODE` | `INTRASTATTRANSACTIONS.NOMENCLATUREINTRACEECODE = INTRASTATCOMBINEDNOMENCLATURE.CODE` |
| `INTRASTATCOMBINEDNOMENCLATURE_INTRASTAT` | [`CHARGES`](../OTHER/CHARGES.md) | `INTRASTATCODE` | `CHARGES.INTRASTATCODE = INTRASTATCOMBINEDNOMENCLATURE.CODE` |
| `INTRASTATCOMBINEDNOMENCLATURE_INTRASTAT` | [`NONINVENTORY`](../INTRASTAT/NONINVENTORY.md) | `INTRASTATCODE` | `NONINVENTORY.INTRASTATCODE = INTRASTATCOMBINEDNOMENCLATURE.CODE` |
| `INTRASTATCOMBINEDNOMENCLATURE_INTRASTAT` | [`TOOL`](../CORE_MASTER/TOOL.md) | `INTRASTATCODE` | `TOOL.INTRASTATCODE = INTRASTATCOMBINEDNOMENCLATURE.CODE` |
| `INTRASTATCOMBINEDNOMENCLATURE_INTRASTAT` | [`PRODUCT`](../ITEM_MASTER/PRODUCT.md) | `INTRASTATCODE` | `PRODUCT.INTRASTATCODE = INTRASTATCOMBINEDNOMENCLATURE.CODE` |
| `INTRASTATCOMBINEDNOMENCLATURE_INTRASTAT` | [`SERVICES`](../COSTING/SERVICES.md) | `INTRASTATCODE` | `SERVICES.INTRASTATCODE = INTRASTATCOMBINEDNOMENCLATURE.CODE` |
| `INTRASTATCOMBINEDNOMENCLATURE_INTRASTAT` | [`CONTAINER`](../CORE_MASTER/CONTAINER.md) | `INTRASTATCODE` | `CONTAINER.INTRASTATCODE = INTRASTATCOMBINEDNOMENCLATURE.CODE` |
| `INTRASTATCOMBINEDNOMENCLATURE_NOMENCLATUREINTRACEE` | [`INTRASTATDECLARATIONROW`](../INTRASTAT/INTRASTATDECLARATIONROW.md) | `NOMENCLATUREINTRACEECODE` | `INTRASTATDECLARATIONROW.NOMENCLATUREINTRACEECODE = INTRASTATCOMBINEDNOMENCLATURE.CODE` |

## Indexes

- `RASTATCOMBINEDNOMENCLATUREUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.EXCLUDEDINTEREEC,
       t.SUPPLUMREQUIRED,
       t.SUPPLEMENTARYUMCODE,
       t.INTRASTATTRNLINEPOLICYCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.INTRASTATCOMBINEDNOMENCLATURE t
FETCH FIRST 100 ROWS ONLY;
```
