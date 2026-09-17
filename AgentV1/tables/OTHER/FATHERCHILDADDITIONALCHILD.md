# DB2ADMIN.FATHERCHILDADDITIONALCHILD

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `FATHERITEMTYPECODE`, `CHILDITEMTYPECODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 207333

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FATHERITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CHILDITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `NROFROWS` | INTEGER | NOT NULL |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FATHERCHILDADDITIONALCHILD.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `FATHERCHILDITEMTYPE_ADDITIONALCHILDS` | `COMPANYCODE`, `FATHERITEMTYPECODE`, `CHILDITEMTYPECODE` | [`FATHERCHILDITEMTYPE`](../OTHER/FATHERCHILDITEMTYPE.md) | `COMPANYCODE`, `FATHERITEMTYPECODE`, `CHILDITEMTYPECODE` | RESTRICT | `FATHERCHILDADDITIONALCHILD.COMPANYCODE = FATHERCHILDITEMTYPE.COMPANYCODE AND FATHERCHILDADDITIONALCHILD.FATHERITEMTYPECODE = FATHERCHILDITEMTYPE.FATHERITEMTYPECODE AND FATHERCHILDADDITIONALCHILD.CHILDITEMTYPECODE = FATHERCHILDITEMTYPE.CHILDITEMTYPECODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FATHERCHILDADDITIONALCHILD.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND FATHERCHILDADDITIONALCHILD.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FATHERCHILDADDITIONALCHILDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FATHERITEMTYPECODE,
       t.CHILDITEMTYPECODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.NROFROWS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.FATHERCHILDADDITIONALCHILD t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
