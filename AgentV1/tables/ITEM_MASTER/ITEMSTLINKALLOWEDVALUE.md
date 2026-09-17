# DB2ADMIN.ITEMSTLINKALLOWEDVALUE

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'ITEM')
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `ITEMSTLINKLINKITEMTYPECMYCODE`, `ITEMSTLINKLINKITEMTYPECODE`, `ITEMSTLINKLINKPOSITION`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 13823

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ITEMSTLINKLINKITEMTYPECMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ITEMSTLINKLINKITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMSTLINKLINKPOSITION` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 4 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 14 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 15 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 16 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 25 | `SAMPLE` | SMALLINT | NOT NULL |  |  |  |
| 26 | `OBSOLETE` | SMALLINT | NOT NULL |  |  |  |
| 27 | `PROTOTYPETEMPORARY` | SMALLINT | NOT NULL |  |  |  |
| 28 | `APPROVALSTATUS` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ITEMSTLINKALLOWEDVALUE.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `ITEMSTLINK_ALLOWEDVALUE` | `ITEMSTLINKLINKITEMTYPECMYCODE`, `ITEMSTLINKLINKITEMTYPECODE`, `ITEMSTLINKLINKPOSITION` | [`ITEMSTLINK`](../ITEM_MASTER/ITEMSTLINK.md) | `LINKITEMTYPECOMPANYCODE`, `LINKITEMTYPECODE`, `LINKPOSITION` | RESTRICT | `ITEMSTLINKALLOWEDVALUE.ITEMSTLINKLINKITEMTYPECMYCODE = ITEMSTLINK.LINKITEMTYPECOMPANYCODE AND ITEMSTLINKALLOWEDVALUE.ITEMSTLINKLINKITEMTYPECODE = ITEMSTLINK.LINKITEMTYPECODE AND ITEMSTLINKALLOWEDVALUE.ITEMSTLINKLINKPOSITION = ITEMSTLINK.LINKPOSITION` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITEMSTLINKALLOWEDVALUEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ITEMSTLINKLINKITEMTYPECMYCODE,
       t.ITEMSTLINKLINKITEMTYPECODE,
       t.ITEMSTLINKLINKPOSITION,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08,
       t.SUBCODE09
FROM   DB2ADMIN.ITEMSTLINKALLOWEDVALUE t
FETCH FIRST 100 ROWS ONLY;
```
