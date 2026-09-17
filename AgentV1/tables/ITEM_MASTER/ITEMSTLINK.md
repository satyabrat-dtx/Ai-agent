# DB2ADMIN.ITEMSTLINK

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'ITEM')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `LINKITEMTYPECOMPANYCODE`, `LINKITEMTYPECODE`, `LINKPOSITION`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 17442

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LINKITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `LINKITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINKPOSITION` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SUBCODE01LINKED` | SMALLINT | NOT NULL |  |  |  |
| 4 | `SUBCODE02LINKED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `SUBCODE03LINKED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `SUBCODE04LINKED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `SUBCODE05LINKED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `SUBCODE06LINKED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `SUBCODE07LINKED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `SUBCODE08LINKED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `SUBCODE09LINKED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `LOGICLINK` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `USERLINKCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `USERLINKCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ITEMSTLINK.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `ITEMSUBCODETEMPLATE_LINK` | `LINKITEMTYPECOMPANYCODE`, `LINKITEMTYPECODE`, `LINKPOSITION` | [`ITEMSUBCODETEMPLATE`](../ITEM_MASTER/ITEMSUBCODETEMPLATE.md) | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE`, `POSITION` | RESTRICT | `ITEMSTLINK.LINKITEMTYPECOMPANYCODE = ITEMSUBCODETEMPLATE.ITEMTYPECOMPANYCODE AND ITEMSTLINK.LINKITEMTYPECODE = ITEMSUBCODETEMPLATE.ITEMTYPECODE AND ITEMSTLINK.LINKPOSITION = ITEMSUBCODETEMPLATE.POSITION` |
| `USERGLINKTYPE_USERLINK` | `USERLINKCOMPANYCODE`, `USERLINKCODE` | [`USERGLINKTYPE`](../ITEM_MASTER/USERGLINKTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMSTLINK.USERLINKCOMPANYCODE = USERGLINKTYPE.COMPANYCODE AND ITEMSTLINK.USERLINKCODE = USERGLINKTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ITEMSTLINK_ALLOWEDVALUE` | [`ITEMSTLINKALLOWEDVALUE`](../ITEM_MASTER/ITEMSTLINKALLOWEDVALUE.md) | `ITEMSTLINKLINKITEMTYPECMYCODE`, `ITEMSTLINKLINKITEMTYPECODE`, `ITEMSTLINKLINKPOSITION` | `ITEMSTLINKALLOWEDVALUE.ITEMSTLINKLINKITEMTYPECMYCODE = ITEMSTLINK.LINKITEMTYPECOMPANYCODE AND ITEMSTLINKALLOWEDVALUE.ITEMSTLINKLINKITEMTYPECODE = ITEMSTLINK.LINKITEMTYPECODE AND ITEMSTLINKALLOWEDVALUE.ITEMSTLINKLINKPOSITION = ITEMSTLINK.LINKPOSITION` |

## Indexes

- `ITEMSTLINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.LINKITEMTYPECOMPANYCODE,
       t.LINKITEMTYPECODE,
       t.LINKPOSITION,
       t.SUBCODE01LINKED,
       t.SUBCODE02LINKED,
       t.SUBCODE03LINKED,
       t.SUBCODE04LINKED,
       t.SUBCODE05LINKED,
       t.SUBCODE06LINKED,
       t.SUBCODE07LINKED,
       t.SUBCODE08LINKED,
       t.SUBCODE09LINKED
FROM   DB2ADMIN.ITEMSTLINK t
FETCH FIRST 100 ROWS ONLY;
```
