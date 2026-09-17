# DB2ADMIN.QUICKRULECONFIGMAPPING

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `QUICKRULECONFIGCOMPANYCODE`, `QUICKRULECONFIGCODE`, `FATHERITEMTYPECODE`, `COMPONENTITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 199201

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `QUICKRULECONFIGCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `QUICKRULECONFIGCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FATHERITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `FATHERITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `COMPONENTITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 5 | `COMPONENTITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `RULECODE` | CHAR(10) |  | FK | foreign_key |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `RULEUSABILITY` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ITEMTYPE_COMPONENTITEMTYPE` | `COMPONENTITEMTYPECOMPANYCODE`, `COMPONENTITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUICKRULECONFIGMAPPING.COMPONENTITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND QUICKRULECONFIGMAPPING.COMPONENTITEMTYPECODE = ITEMTYPE.CODE` |
| `ITEMTYPE_FATHERITEMTYPE` | `FATHERITEMTYPECOMPANYCODE`, `FATHERITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUICKRULECONFIGMAPPING.FATHERITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND QUICKRULECONFIGMAPPING.FATHERITEMTYPECODE = ITEMTYPE.CODE` |
| `QUICKRULECONFIG_MAPPINGS` | `QUICKRULECONFIGCOMPANYCODE`, `QUICKRULECONFIGCODE` | [`QUICKRULECONFIG`](../OTHER/QUICKRULECONFIG.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUICKRULECONFIGMAPPING.QUICKRULECONFIGCOMPANYCODE = QUICKRULECONFIG.COMPANYCODE AND QUICKRULECONFIGMAPPING.QUICKRULECONFIGCODE = QUICKRULECONFIG.CODE` |
| `RULES_RULE` | `QUICKRULECONFIGCOMPANYCODE`, `RULECODE` | [`RULES`](../CORE_MASTER/RULES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUICKRULECONFIGMAPPING.QUICKRULECONFIGCOMPANYCODE = RULES.COMPANYCODE AND QUICKRULECONFIGMAPPING.RULECODE = RULES.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QUICKRULECONFIGMAPPINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.QUICKRULECONFIGCOMPANYCODE,
       t.QUICKRULECONFIGCODE,
       t.FATHERITEMTYPECOMPANYCODE,
       t.FATHERITEMTYPECODE,
       t.COMPONENTITEMTYPECOMPANYCODE,
       t.COMPONENTITEMTYPECODE,
       t.RULECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.QUICKRULECONFIGMAPPING t
FETCH FIRST 100 ROWS ONLY;
```
