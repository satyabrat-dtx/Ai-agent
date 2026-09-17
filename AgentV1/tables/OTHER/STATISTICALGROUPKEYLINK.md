# DB2ADMIN.STATISTICALGROUPKEYLINK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 20687

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SUBCODE01REQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 3 | `SUBCODE02REQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 4 | `SUBCODE03REQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `SUBCODE04REQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `SUBCODE05REQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `SUBCODE06REQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `SUBCODE07REQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `SUBCODE08REQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `SUBCODE09REQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `SUBCODE10REQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 17 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `STATISTICALGROUPKEYLINK.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `STATISTICALGROUPKEYLINK.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `STATISTICALGROUPKEYLINK.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND STATISTICALGROUPKEYLINK.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `STATISTICALGROUPKEYLINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01REQUIRED,
       t.SUBCODE02REQUIRED,
       t.SUBCODE03REQUIRED,
       t.SUBCODE04REQUIRED,
       t.SUBCODE05REQUIRED,
       t.SUBCODE06REQUIRED,
       t.SUBCODE07REQUIRED,
       t.SUBCODE08REQUIRED,
       t.SUBCODE09REQUIRED,
       t.SUBCODE10REQUIRED
FROM   DB2ADMIN.STATISTICALGROUPKEYLINK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
