# DB2ADMIN.FATHERCHILDITEMTYPE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 42
- **Primary key**: `COMPANYCODE`, `FATHERITEMTYPECODE`, `CHILDITEMTYPECODE`
- **FK degree**: referenced by 1 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 118118

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FATHERITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `FATHERITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CHILDITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `CHILDITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `CREATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 6 | `PRIMARYCONVERSION` | SMALLINT | NOT NULL |  |  |  |
| 7 | `SECONDARYCONVERSION` | SMALLINT | NOT NULL |  |  |  |
| 8 | `PACKAGINGCONVERSION` | SMALLINT | NOT NULL |  |  |  |
| 9 | `STLINKALLOWEDVALUES` | SMALLINT | NOT NULL |  |  |  |
| 10 | `PRODUCTALLOWEDVALUES` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ADDITIONALDATA` | SMALLINT | NOT NULL |  |  |  |
| 12 | `LINKSUBCODES` | SMALLINT | NOT NULL |  |  |  |
| 13 | `SUBCODE01LINKTO` | INTEGER | NOT NULL |  |  |  |
| 14 | `SUBCODE02LINKTO` | INTEGER | NOT NULL |  |  |  |
| 15 | `SUBCODE03LINKTO` | INTEGER | NOT NULL |  |  |  |
| 16 | `SUBCODE04LINKTO` | INTEGER | NOT NULL |  |  |  |
| 17 | `SUBCODE05LINKTO` | INTEGER | NOT NULL |  |  |  |
| 18 | `SUBCODE06LINKTO` | INTEGER | NOT NULL |  |  |  |
| 19 | `SUBCODE07LINKTO` | INTEGER | NOT NULL |  |  |  |
| 20 | `SUBCODE08LINKTO` | INTEGER | NOT NULL |  |  |  |
| 21 | `SUBCODE09LINKTO` | INTEGER | NOT NULL |  |  |  |
| 22 | `SUBCODE10LINKTO` | INTEGER | NOT NULL |  |  |  |
| 23 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 24 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 25 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 26 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 29 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 31 | `LINKBOMSUBCODES` | SMALLINT | NOT NULL |  |  |  |
| 32 | `BOMSUBCODE01LINKTO` | INTEGER | NOT NULL |  |  |  |
| 33 | `BOMSUBCODE02LINKTO` | INTEGER | NOT NULL |  |  |  |
| 34 | `BOMSUBCODE03LINKTO` | INTEGER | NOT NULL |  |  |  |
| 35 | `BOMSUBCODE04LINKTO` | INTEGER | NOT NULL |  |  |  |
| 36 | `BOMSUBCODE05LINKTO` | INTEGER | NOT NULL |  |  |  |
| 37 | `BOMSUBCODE06LINKTO` | INTEGER | NOT NULL |  |  |  |
| 38 | `BOMSUBCODE07LINKTO` | INTEGER | NOT NULL |  |  |  |
| 39 | `BOMSUBCODE08LINKTO` | INTEGER | NOT NULL |  |  |  |
| 40 | `BOMSUBCODE09LINKTO` | INTEGER | NOT NULL |  |  |  |
| 41 | `BOMSUBCODE10LINKTO` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FATHERCHILDITEMTYPE.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FATHERCHILDITEMTYPE.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_CHILDITEMTYPE` | `CHILDITEMTYPECOMPANYCODE`, `CHILDITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FATHERCHILDITEMTYPE.CHILDITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND FATHERCHILDITEMTYPE.CHILDITEMTYPECODE = ITEMTYPE.CODE` |
| `ITEMTYPE_FATHERITEMTYPE` | `FATHERITEMTYPECOMPANYCODE`, `FATHERITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FATHERCHILDITEMTYPE.FATHERITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND FATHERCHILDITEMTYPE.FATHERITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FATHERCHILDITEMTYPE_ADDITIONALCHILDS` | [`FATHERCHILDADDITIONALCHILD`](../OTHER/FATHERCHILDADDITIONALCHILD.md) | `COMPANYCODE`, `FATHERITEMTYPECODE`, `CHILDITEMTYPECODE` | `FATHERCHILDADDITIONALCHILD.COMPANYCODE = FATHERCHILDITEMTYPE.COMPANYCODE AND FATHERCHILDADDITIONALCHILD.FATHERITEMTYPECODE = FATHERCHILDITEMTYPE.FATHERITEMTYPECODE AND FATHERCHILDADDITIONALCHILD.CHILDITEMTYPECODE = FATHERCHILDITEMTYPE.CHILDITEMTYPECODE` |

## Indexes

- `FATHERCHILDITEMTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FATHERITEMTYPECOMPANYCODE,
       t.FATHERITEMTYPECODE,
       t.CHILDITEMTYPECOMPANYCODE,
       t.CHILDITEMTYPECODE,
       t.CREATIONPOLICYCODE,
       t.PRIMARYCONVERSION,
       t.SECONDARYCONVERSION,
       t.PACKAGINGCONVERSION,
       t.STLINKALLOWEDVALUES,
       t.PRODUCTALLOWEDVALUES,
       t.ADDITIONALDATA
FROM   DB2ADMIN.FATHERCHILDITEMTYPE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
