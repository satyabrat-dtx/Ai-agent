# DB2ADMIN.SELLINGITEMTYPESUBCODESLINK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `COMPANYCODE`, `SELLINGITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 6700

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SELLINGITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INTERNALITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 3 | `SUBCODE01LINKTO` | INTEGER | NOT NULL |  |  |  |
| 4 | `SUBCODE02LINKTO` | INTEGER | NOT NULL |  |  |  |
| 5 | `SUBCODE03LINKTO` | INTEGER | NOT NULL |  |  |  |
| 6 | `SUBCODE04LINKTO` | INTEGER | NOT NULL |  |  |  |
| 7 | `SUBCODE05LINKTO` | INTEGER | NOT NULL |  |  |  |
| 8 | `SUBCODE06LINKTO` | INTEGER | NOT NULL |  |  |  |
| 9 | `SUBCODE07LINKTO` | INTEGER | NOT NULL |  |  |  |
| 10 | `SUBCODE08LINKTO` | INTEGER | NOT NULL |  |  |  |
| 11 | `SUBCODE09LINKTO` | INTEGER | NOT NULL |  |  |  |
| 12 | `SUBCODE10LINKTO` | INTEGER | NOT NULL |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `SELLINGITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 18 | `INTERNALITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SELLINGITEMTYPESUBCODESLINK.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_INTERNALITEMTYPE` | `INTERNALITEMTYPECOMPANYCODE`, `INTERNALITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SELLINGITEMTYPESUBCODESLINK.INTERNALITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND SELLINGITEMTYPESUBCODESLINK.INTERNALITEMTYPECODE = ITEMTYPE.CODE` |
| `ITEMTYPE_SELLINGITEMTYPE` | `SELLINGITEMTYPECOMPANYCODE`, `SELLINGITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SELLINGITEMTYPESUBCODESLINK.SELLINGITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND SELLINGITEMTYPESUBCODESLINK.SELLINGITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LINGITEMTYPESUBCODESLINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SELLINGITEMTYPECODE,
       t.INTERNALITEMTYPECODE,
       t.SUBCODE01LINKTO,
       t.SUBCODE02LINKTO,
       t.SUBCODE03LINKTO,
       t.SUBCODE04LINKTO,
       t.SUBCODE05LINKTO,
       t.SUBCODE06LINKTO,
       t.SUBCODE07LINKTO,
       t.SUBCODE08LINKTO,
       t.SUBCODE09LINKTO
FROM   DB2ADMIN.SELLINGITEMTYPESUBCODESLINK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
