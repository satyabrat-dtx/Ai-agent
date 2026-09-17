# DB2ADMIN.LOGBILLOFEXCHANGE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 46
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 200837

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `CODE` | CHAR(12) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `BILLOFEXCHANGEDATE` | DATE | NOT NULL |  |  |  |
| 4 | `HEADERLINE1` | CHAR(50) |  |  |  |  |
| 5 | `HEADERLINE2` | CHAR(50) |  |  |  |  |
| 6 | `HEADERLINE3` | CHAR(50) |  |  |  |  |
| 7 | `HEADERLINE4` | CHAR(50) |  |  |  |  |
| 8 | `HEADERLINE5` | CHAR(50) |  |  |  |  |
| 9 | `AMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `PAYMENTTEMRSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `PAYMENTTEMRSCODE` | CHAR(3) |  |  |  |  |
| 12 | `INVOICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 13 | `DUEDATE` | DATE |  |  |  |  |
| 14 | `DAYSAFTER` | VARCHAR(100) |  |  |  |  |
| 15 | `PAYTOORDER` | VARCHAR(100) |  |  |  |  |
| 16 | `AMOUNTINWORD` | VARCHAR(250) |  |  |  |  |
| 17 | `NOOFCARTONS` | INTEGER | NOT NULL |  |  |  |
| 18 | `SSAIRBY` | CHAR(25) |  |  |  |  |
| 19 | `BLAWBNO` | CHAR(25) |  |  |  |  |
| 20 | `BLAWBDATE` | DATE |  |  |  |  |
| 21 | `BETO` | VARCHAR(250) |  |  |  |  |
| 22 | `BUYERSBANK` | VARCHAR(250) |  |  |  |  |
| 23 | `PLACE` | CHAR(50) |  |  |  |  |
| 24 | `LCBENEFICIARYBANKBANKCNYCODE` | CHAR(3) |  |  |  |  |
| 25 | `LCBENEFICIARYBANKCODE` | CHAR(15) |  |  |  |  |
| 26 | `LCBENEFICIARYBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 27 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 28 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 29 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 30 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 31 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 32 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 33 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 34 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 35 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 36 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 37 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 38 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 39 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 40 | `STATUS` | CHAR(2) |  |  |  |  |
| 41 | `BANKREFNO` | CHAR(30) |  |  |  |  |
| 42 | `LCDETAILLCNO` | CHAR(35) |  |  |  |  |
| 43 | `LCDETAILLCDATE` | DATE |  |  |  |  |
| 44 | `LCBENEFICIARYIDIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 45 | `LCBENEFICIARYACCNO` | CHAR(30) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGBILLOFEXCHANGE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGBILLOFEXCHANGECHECKLIST`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)
- child `LOGBILLOFEXCHANGEDETAIL`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGBILLOFEXCHANGEDOCUMENTS`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CODE,
       t.BILLOFEXCHANGEDATE,
       t.HEADERLINE1,
       t.HEADERLINE2,
       t.HEADERLINE3,
       t.HEADERLINE4,
       t.HEADERLINE5,
       t.AMOUNT,
       t.PAYMENTTEMRSCOMPANYCODE,
       t.PAYMENTTEMRSCODE
FROM   DB2ADMIN.LOGBILLOFEXCHANGE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
