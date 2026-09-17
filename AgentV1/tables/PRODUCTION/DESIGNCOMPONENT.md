# DB2ADMIN.DESIGNCOMPONENT

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `DESIGNCOMPANYCODE`, `DESIGNNUMBERID`, `VARIANTCODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 29299

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DESIGNCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `DESIGNNUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DESIGNITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 3 | `DESIGNSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 4 | `DESIGNSUBCODE02` | CHAR(10) |  |  |  |  |
| 5 | `DESIGNSUBCODE03` | CHAR(10) |  |  |  |  |
| 6 | `DESIGNSUBCODE04` | CHAR(10) |  |  |  |  |
| 7 | `DESIGNSUBCODE05` | CHAR(10) |  |  |  |  |
| 8 | `DESIGNSUBCODE06` | CHAR(10) |  |  |  |  |
| 9 | `DESIGNSUBCODE07` | CHAR(10) |  |  |  |  |
| 10 | `DESIGNSUBCODE08` | CHAR(10) |  |  |  |  |
| 11 | `DESIGNSUBCODE09` | CHAR(10) |  |  |  |  |
| 12 | `DESIGNSUBCODE10` | CHAR(10) |  |  |  |  |
| 13 | `DESIGNSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 14 | `VARIANTCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 15 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 16 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 17 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 18 | `IMAGENAME` | CHAR(50) |  |  |  |  |
| 19 | `IMAGEPATH` | CHAR(30) |  |  |  |  |
| 20 | `INITIALDATE` | DATE |  |  |  |  |
| 21 | `FINALDATE` | DATE |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 27 | `DESIGNITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 28 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 29 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DESIGN_DESIGNCOMPONENT` | `DESIGNCOMPANYCODE`, `DESIGNNUMBERID` | [`DESIGN`](../PRODUCTION/DESIGN.md) | `COMPANYCODE`, `NUMBERID` | RESTRICT | `DESIGNCOMPONENT.DESIGNCOMPANYCODE = DESIGN.COMPANYCODE AND DESIGNCOMPONENT.DESIGNNUMBERID = DESIGN.NUMBERID` |
| `ITEMTYPE_DESIGNITEMTYPE` | `DESIGNITEMTYPECOMPANYCODE`, `DESIGNITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DESIGNCOMPONENT.DESIGNITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND DESIGNCOMPONENT.DESIGNITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `DESIGNCOMPONENT_DESIGNSCREENS` | [`DESIGNSCREENS`](../PRODUCTION/DESIGNSCREENS.md) | `DESIGNCMPDESIGNCOMPANYCODE`, `DESIGNCOMPONENTDESIGNNUMBERID`, `DESIGNCOMPONENTVARIANTCODE` | `DESIGNSCREENS.DESIGNCMPDESIGNCOMPANYCODE = DESIGNCOMPONENT.DESIGNCOMPANYCODE AND DESIGNSCREENS.DESIGNCOMPONENTDESIGNNUMBERID = DESIGNCOMPONENT.DESIGNNUMBERID AND DESIGNSCREENS.DESIGNCOMPONENTVARIANTCODE = DESIGNCOMPONENT.VARIANTCODE` |

## Indexes

- `DESIGNCOMPONENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DESIGNCOMPANYCODE,
       t.DESIGNNUMBERID,
       t.DESIGNITEMTYPECODE,
       t.DESIGNSUBCODE01,
       t.DESIGNSUBCODE02,
       t.DESIGNSUBCODE03,
       t.DESIGNSUBCODE04,
       t.DESIGNSUBCODE05,
       t.DESIGNSUBCODE06,
       t.DESIGNSUBCODE07,
       t.DESIGNSUBCODE08,
       t.DESIGNSUBCODE09
FROM   DB2ADMIN.DESIGNCOMPONENT t
FETCH FIRST 100 ROWS ONLY;
```
