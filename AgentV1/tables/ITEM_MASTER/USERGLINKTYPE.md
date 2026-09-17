# DB2ADMIN.USERGLINKTYPE

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 3219

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `DATATYPE` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `CODEMAXLENGTH` | INTEGER | NOT NULL |  |  |  |
| 7 | `GROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `DETAILDATATYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `DETAILCODEMAXLENGTH` | INTEGER | NOT NULL |  |  |  |
| 10 | `DETAILGROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `GROUPTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 18 | `DETAILGROUPTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `USERGLINKTYPE.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `USERGLINKTYPE.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `USERGENERICGROUPTYPE_DETAILGROUPTYPE` | `DETAILGROUPTYPECOMPANYCODE`, `DETAILGROUPTYPECODE` | [`USERGENERICGROUPTYPE`](../CORE_MASTER/USERGENERICGROUPTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `USERGLINKTYPE.DETAILGROUPTYPECOMPANYCODE = USERGENERICGROUPTYPE.COMPANYCODE AND USERGLINKTYPE.DETAILGROUPTYPECODE = USERGENERICGROUPTYPE.CODE` |
| `USERGENERICGROUPTYPE_GROUPTYPE` | `GROUPTYPECOMPANYCODE`, `GROUPTYPECODE` | [`USERGENERICGROUPTYPE`](../CORE_MASTER/USERGENERICGROUPTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `USERGLINKTYPE.GROUPTYPECOMPANYCODE = USERGENERICGROUPTYPE.COMPANYCODE AND USERGLINKTYPE.GROUPTYPECODE = USERGENERICGROUPTYPE.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `USERGLINKTYPE_GROUP` | [`USERGLINK`](../ITEM_MASTER/USERGLINK.md) | `USERGLINKTYPECOMPANYCODE`, `USERGLINKTYPECODE` | `USERGLINK.USERGLINKTYPECOMPANYCODE = USERGLINKTYPE.COMPANYCODE AND USERGLINK.USERGLINKTYPECODE = USERGLINKTYPE.CODE` |
| `USERGLINKTYPE_USERLINK` | [`ITEMSTLINK`](../ITEM_MASTER/ITEMSTLINK.md) | `USERLINKCOMPANYCODE`, `USERLINKCODE` | `ITEMSTLINK.USERLINKCOMPANYCODE = USERGLINKTYPE.COMPANYCODE AND ITEMSTLINK.USERLINKCODE = USERGLINKTYPE.CODE` |

## Indexes

- `USERGLINKTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.DATATYPE,
       t.CODEMAXLENGTH,
       t.GROUPTYPECODE,
       t.DETAILDATATYPE,
       t.DETAILCODEMAXLENGTH,
       t.DETAILGROUPTYPECODE,
       t.CREATIONDATETIME
FROM   DB2ADMIN.USERGLINKTYPE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
