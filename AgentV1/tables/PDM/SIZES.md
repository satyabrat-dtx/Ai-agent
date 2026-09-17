# DB2ADMIN.SIZES

- **Module**: `PDM` (low confidence — FK neighbourhood: 2 of 2 related tables are PDM)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `SIZESTYPECOMPANYCODE`, `SIZESTYPECODE`, `CODE`
- **FK degree**: referenced by 6 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 7602

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SIZESTYPECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SIZESTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SIZES.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `SIZESTYPE_SIZES` | `SIZESTYPECOMPANYCODE`, `SIZESTYPECODE` | [`SIZESTYPE`](../PDM/SIZESTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SIZES.SIZESTYPECOMPANYCODE = SIZESTYPE.COMPANYCODE AND SIZES.SIZESTYPECODE = SIZESTYPE.CODE` |

## Referenced by (child → this table) — 6

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SIZES_DSLINKEDSIZFI` | [`PDMDB6`](../PDM/PDMDB6.md) | `DSLINKEDSIZFISIZESTYPECMYCODE`, `DSLINKEDSIZFISIZESTYPECODE`, `DSLINKEDSIZFICODE` | `PDMDB6.DSLINKEDSIZFISIZESTYPECMYCODE = SIZES.SIZESTYPECOMPANYCODE AND PDMDB6.DSLINKEDSIZFISIZESTYPECODE = SIZES.SIZESTYPECODE AND PDMDB6.DSLINKEDSIZFICODE = SIZES.CODE` |
| `SIZES_DSSIZFA` | [`PDMDB6`](../PDM/PDMDB6.md) | `DSSIZFASIZESTYPECOMPANYCODE`, `DSSIZFASIZESTYPECODE`, `DSSIZFACODE` | `PDMDB6.DSSIZFASIZESTYPECOMPANYCODE = SIZES.SIZESTYPECOMPANYCODE AND PDMDB6.DSSIZFASIZESTYPECODE = SIZES.SIZESTYPECODE AND PDMDB6.DSSIZFACODE = SIZES.CODE` |
| `SIZES_DSSIZFI` | [`PDMDB6`](../PDM/PDMDB6.md) | `DSSIZFISIZESTYPECOMPANYCODE`, `DSSIZFISIZESTYPECODE`, `DSSIZFICODE` | `PDMDB6.DSSIZFISIZESTYPECOMPANYCODE = SIZES.SIZESTYPECOMPANYCODE AND PDMDB6.DSSIZFISIZESTYPECODE = SIZES.SIZESTYPECODE AND PDMDB6.DSSIZFICODE = SIZES.CODE` |
| `SIZES_DBCDSIZ` | [`PDMDB1`](../PDM/PDMDB1.md) | `DBCDSIZSIZESTYPECOMPANYCODE`, `DBCDSIZSIZESTYPECODE`, `DBCDSIZCODE` | `PDMDB1.DBCDSIZSIZESTYPECOMPANYCODE = SIZES.SIZESTYPECOMPANYCODE AND PDMDB1.DBCDSIZSIZESTYPECODE = SIZES.SIZESTYPECODE AND PDMDB1.DBCDSIZCODE = SIZES.CODE` |
| `SIZES_DBLINKEDCDSIZ` | [`PDMDB1`](../PDM/PDMDB1.md) | `DBLINKEDCDSIZSIZESTYPECMYCODE`, `DBLINKEDCDSIZSIZESTYPECODE`, `DBLINKEDCDSIZCODE` | `PDMDB1.DBLINKEDCDSIZSIZESTYPECMYCODE = SIZES.SIZESTYPECOMPANYCODE AND PDMDB1.DBLINKEDCDSIZSIZESTYPECODE = SIZES.SIZESTYPECODE AND PDMDB1.DBLINKEDCDSIZCODE = SIZES.CODE` |
| `SIZES_SIZE` | [`MARKERLINE`](../OTHER/MARKERLINE.md) | `SIZESIZESTYPECOMPANYCODE`, `SIZESIZESTYPECODE`, `SIZECODE` | `MARKERLINE.SIZESIZESTYPECOMPANYCODE = SIZES.SIZESTYPECOMPANYCODE AND MARKERLINE.SIZESIZESTYPECODE = SIZES.SIZESTYPECODE AND MARKERLINE.SIZECODE = SIZES.CODE` |

## Implicit links (NOT declared in the DDL — inferred)

- child `SIZESALIAS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `SIZESALIASBEAN`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Indexes

- `SIZESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SIZESTYPECOMPANYCODE,
       t.SIZESTYPECODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.SEQUENCE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.OWNINGCOMPANYCODE
FROM   DB2ADMIN.SIZES t
FETCH FIRST 100 ROWS ONLY;
```
