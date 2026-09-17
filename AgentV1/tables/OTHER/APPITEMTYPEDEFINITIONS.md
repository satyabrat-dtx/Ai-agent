# DB2ADMIN.APPITEMTYPEDEFINITIONS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 110783

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `MANAGESTATICALGROUP` | SMALLINT | NOT NULL |  |  |  |
| 4 | `MANAGECOLLECTION` | SMALLINT | NOT NULL |  |  |  |
| 5 | `MANAGEITEMTYPE` | SMALLINT | NOT NULL |  |  |  |
| 6 | `MANAGESUBCODE01` | SMALLINT | NOT NULL |  |  |  |
| 7 | `MANAGESUBCODE02` | SMALLINT | NOT NULL |  |  |  |
| 8 | `MANAGESUBCODE03` | SMALLINT | NOT NULL |  |  |  |
| 9 | `MANAGESUBCODE04` | SMALLINT | NOT NULL |  |  |  |
| 10 | `MANAGESUBCODE05` | SMALLINT | NOT NULL |  |  |  |
| 11 | `MANAGESUBCODE06` | SMALLINT | NOT NULL |  |  |  |
| 12 | `MANAGESUBCODE07` | SMALLINT | NOT NULL |  |  |  |
| 13 | `MANAGESUBCODE08` | SMALLINT | NOT NULL |  |  |  |
| 14 | `MANAGESUBCODE09` | SMALLINT | NOT NULL |  |  |  |
| 15 | `MANAGESUBCODE10` | SMALLINT | NOT NULL |  |  |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `APPITEMTYPEDEFINITIONS.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND APPITEMTYPEDEFINITIONS.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `APPITEMTYPEDEFINITIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.MANAGESTATICALGROUP,
       t.MANAGECOLLECTION,
       t.MANAGEITEMTYPE,
       t.MANAGESUBCODE01,
       t.MANAGESUBCODE02,
       t.MANAGESUBCODE03,
       t.MANAGESUBCODE04,
       t.MANAGESUBCODE05,
       t.MANAGESUBCODE06
FROM   DB2ADMIN.APPITEMTYPEDEFINITIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
