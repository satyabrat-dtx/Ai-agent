# DB2ADMIN.GARMENTCOLORWAYS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODE01`, `COMPTYPECODE`, `GARMENTCOLOR`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 126875

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `USERGENGROUPTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `USERGENERICGROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `GARMENTCOLOR` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 16 | `COMPITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 17 | `COMPITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 18 | `COMPTYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 19 | `COMPCOLOR` | CHAR(10) |  |  |  |  |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `GARMENTCOLORWAYS.COMPANYCODE = COMPANY.CODE` |
| `COMPONENT_COMPTYPE` | `COMPANYCODE`, `COMPTYPECODE` | [`COMPONENT`](../OTHER/COMPONENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GARMENTCOLORWAYS.COMPANYCODE = COMPONENT.COMPANYCODE AND GARMENTCOLORWAYS.COMPTYPECODE = COMPONENT.CODE` |
| `ITEMTYPE_COMPITEMTYPE` | `COMPITEMTYPECOMPANYCODE`, `COMPITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GARMENTCOLORWAYS.COMPITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND GARMENTCOLORWAYS.COMPITEMTYPECODE = ITEMTYPE.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GARMENTCOLORWAYS.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND GARMENTCOLORWAYS.ITEMTYPECODE = ITEMTYPE.CODE` |
| `USERGENERICGROUPTYPE_USERGENERICGROUPTYPE` | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE` | [`USERGENERICGROUPTYPE`](../CORE_MASTER/USERGENERICGROUPTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GARMENTCOLORWAYS.USERGENGROUPTYPECOMPANYCODE = USERGENERICGROUPTYPE.COMPANYCODE AND GARMENTCOLORWAYS.USERGENERICGROUPTYPECODE = USERGENERICGROUPTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `GARMENTCOLORWAYSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.USERGENGROUPTYPECOMPANYCODE,
       t.USERGENERICGROUPTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07
FROM   DB2ADMIN.GARMENTCOLORWAYS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
