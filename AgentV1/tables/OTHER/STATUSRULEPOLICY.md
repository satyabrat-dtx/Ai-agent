# DB2ADMIN.STATUSRULEPOLICY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `STATUSCODE`, `LINENR`, `STATUSRULECOMBINATIONSUBLINE`, `STATUSPOLICYCODECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 190856

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `STATUSCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENR` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `STATUSRULECOMBINATIONSUBLINE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `STATUSPOLICYCODECODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `QUANTITYFROM` | DECIMAL(15,5) |  |  |  |  |
| 7 | `QUANTITYTO` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 8 | `QUANTITYCALCRULECODE` | CHAR(20) |  |  |  |  |
| 9 | `TEMPLATELIST` | VARCHAR(2000) |  |  |  |  |
| 10 | `TEMPLATERULE` | INTEGER | NOT NULL |  |  |  |
| 11 | `ALLOWCHANGE` | SMALLINT | NOT NULL |  |  |  |
| 12 | `NOTIFICATIONMESSAGEMESSAGECODE` | CHAR(8) |  | FK | foreign_key |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 21 | `DIVISIONLIST` | VARCHAR(2000) |  |  |  |  |
| 22 | `DIVISIONRULE` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `NOTIFICATIONMESSAGE_NOTIFICATIONMESSAGE` | `COMPANYCODE`, `NOTIFICATIONMESSAGEMESSAGECODE` | [`NOTIFICATIONMESSAGE`](../OTHER/NOTIFICATIONMESSAGE.md) | `COMPANYCODE`, `MESSAGECODE` | RESTRICT | `STATUSRULEPOLICY.COMPANYCODE = NOTIFICATIONMESSAGE.COMPANYCODE AND STATUSRULEPOLICY.NOTIFICATIONMESSAGEMESSAGECODE = NOTIFICATIONMESSAGE.MESSAGECODE` |
| `STATUSPOLICY_STATUSPOLICYCODE` | `COMPANYCODE`, `STATUSPOLICYCODECODE` | [`STATUSPOLICY`](../OTHER/STATUSPOLICY.md) | `COMPANYCODE`, `CODE` | RESTRICT | `STATUSRULEPOLICY.COMPANYCODE = STATUSPOLICY.COMPANYCODE AND STATUSRULEPOLICY.STATUSPOLICYCODECODE = STATUSPOLICY.CODE` |
| `STATUSRULECOMBINATION_STATUSRULEPOLICYLIST` | `COMPANYCODE`, `ITEMTYPECODE`, `STATUSCODE`, `LINENR`, `STATUSRULECOMBINATIONSUBLINE` | [`STATUSRULECOMBINATION`](../OTHER/STATUSRULECOMBINATION.md) | `COMPANYCODE`, `ITEMTYPECODE`, `STATUSCODE`, `LINENR`, `SUBLINE` | RESTRICT | `STATUSRULEPOLICY.COMPANYCODE = STATUSRULECOMBINATION.COMPANYCODE AND STATUSRULEPOLICY.ITEMTYPECODE = STATUSRULECOMBINATION.ITEMTYPECODE AND STATUSRULEPOLICY.STATUSCODE = STATUSRULECOMBINATION.STATUSCODE AND STATUSRULEPOLICY.LINENR = STATUSRULECOMBINATION.LINENR AND STATUSRULEPOLICY.STATUSRULECOMBINATIONSUBLINE = STATUSRULECOMBINATION.SUBLINE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `STATUSRULEPOLICYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.STATUSCODE,
       t.LINENR,
       t.STATUSRULECOMBINATIONSUBLINE,
       t.STATUSPOLICYCODECODE,
       t.QUANTITYFROM,
       t.QUANTITYTO,
       t.QUANTITYCALCRULECODE,
       t.TEMPLATELIST,
       t.TEMPLATERULE,
       t.ALLOWCHANGE
FROM   DB2ADMIN.STATUSRULEPOLICY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
