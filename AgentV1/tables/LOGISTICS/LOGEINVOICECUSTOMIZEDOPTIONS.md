# DB2ADMIN.LOGEINVOICECUSTOMIZEDOPTIONS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 64
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 236610

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COMPANYBUSINESSPARTNERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 2 | `PAUSEMONITORTHREADS` | SMALLINT | NOT NULL |  |  |  |
| 3 | `TAXREGIMECODE` | CHAR(4) |  |  |  |  |
| 4 | `TRANSMITTERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 5 | `TRANSMITTERPOLICYCODE` | CHAR(20) |  |  |  |  |
| 6 | `AUTOMATICLINESDESCRIPTION` | VARCHAR(200) | NOT NULL |  |  |  |
| 7 | `SALESATTACHMENTS` | SMALLINT | NOT NULL |  |  |  |
| 8 | `LINKEDSPOOLFILETYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `SALESASYNCXMLGENERATION` | SMALLINT | NOT NULL |  |  |  |
| 10 | `SALESATTACHMENTSFILEPATH` | VARCHAR(250) |  |  |  |  |
| 11 | `SALESXMLFILEPATH` | VARCHAR(250) |  |  |  |  |
| 12 | `PURCHASESATTACHMENTSFILEPATH` | VARCHAR(250) |  |  |  |  |
| 13 | `PURCHASESXMLFILEPATH` | VARCHAR(250) |  |  |  |  |
| 14 | `PURCHASESIMPORTFILEPATH` | VARCHAR(250) |  |  |  |  |
| 15 | `REA` | SMALLINT | NOT NULL |  |  |  |
| 16 | `REAOFFICECODE` | CHAR(2) |  |  |  |  |
| 17 | `REANUMBER` | CHAR(20) |  |  |  |  |
| 18 | `REASHARECAPITAL` | DECIMAL(14,2) |  |  |  |  |
| 19 | `REAUNIQUEPARTNER` | SMALLINT | NOT NULL |  |  |  |
| 20 | `REALIQUIDATION` | SMALLINT | NOT NULL |  |  |  |
| 21 | `MAXRETRIES` | INTEGER | NOT NULL |  |  |  |
| 22 | `STOPONSENDINGERRORS` | SMALLINT | NOT NULL |  |  |  |
| 23 | `ATOAUTHURL` | VARCHAR(250) |  |  |  |  |
| 24 | `ATIXFEBASEURL` | VARCHAR(250) |  |  |  |  |
| 25 | `ATAOOUID` | VARCHAR(100) |  |  |  |  |
| 26 | `ATUOUID` | CHAR(10) |  |  |  |  |
| 27 | `ATCLIENTID` | VARCHAR(100) |  |  |  |  |
| 28 | `ATCLIENTSECRETENCRYPTED` | VARCHAR(100) |  |  |  |  |
| 29 | `ATUSERNAME` | CHAR(30) |  |  |  |  |
| 30 | `ATPASSWORDENCRYPTED` | VARCHAR(60) |  |  |  |  |
| 31 | `ATDEVICETOKENENCRYPTED` | VARCHAR(1500) |  |  |  |  |
| 32 | `ATCONNECTTIMEOUT` | INTEGER | NOT NULL |  |  |  |
| 33 | `ATREADTIMEOUT` | INTEGER | NOT NULL |  |  |  |
| 34 | `ATTOKENRENEWALADVANCESECONDS` | INTEGER | NOT NULL |  |  |  |
| 35 | `ATLOGINATTEMPTS` | INTEGER | NOT NULL |  |  |  |
| 36 | `ATLOGINRETRYDELAYMS` | INTEGER | NOT NULL |  |  |  |
| 37 | `ATTRANSNOTIFICATIONSBATCHCOUNT` | INTEGER | NOT NULL |  |  |  |
| 38 | `ATRECNOTIFICATIONSBATCHCOUNT` | INTEGER | NOT NULL |  |  |  |
| 39 | `ATTRANSLASTNOTIFICATIONID` | CHAR(50) |  |  |  |  |
| 40 | `ATRECLASTNOTIFICATIONID` | CHAR(50) |  |  |  |  |
| 41 | `ICSERVICEURL` | VARCHAR(250) |  |  |  |  |
| 42 | `ICSERVICEPARTNERID` | VARCHAR(100) |  |  |  |  |
| 43 | `ICSERVICEUSERNAME` | CHAR(30) |  |  |  |  |
| 44 | `ICPASSWORDENCRYPTED` | VARCHAR(60) |  |  |  |  |
| 45 | `ICPURCHASESPDFFILEPATH` | VARCHAR(250) |  |  |  |  |
| 46 | `ICPURCHASESZIPFILEPATH` | VARCHAR(250) |  |  |  |  |
| 47 | `ICCONNECTTIMEOUT` | INTEGER | NOT NULL |  |  |  |
| 48 | `ICREADTIMEOUT` | INTEGER | NOT NULL |  |  |  |
| 49 | `ICSALESLASTNOTIFICATIONID` | BIGINT | NOT NULL |  |  |  |
| 50 | `ICPURCHASESLASTNOTIFICATIONID` | BIGINT | NOT NULL |  |  |  |
| 51 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 52 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 53 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 54 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 55 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 56 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 57 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 58 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 59 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 60 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 61 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 62 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 63 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGEINVOICECUSTOMIZEDOPTIONS.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COMPANYBUSINESSPARTNERNUMBERID,
       t.PAUSEMONITORTHREADS,
       t.TAXREGIMECODE,
       t.TRANSMITTERNUMBERID,
       t.TRANSMITTERPOLICYCODE,
       t.AUTOMATICLINESDESCRIPTION,
       t.SALESATTACHMENTS,
       t.LINKEDSPOOLFILETYPECODE,
       t.SALESASYNCXMLGENERATION,
       t.SALESATTACHMENTSFILEPATH,
       t.SALESXMLFILEPATH
FROM   DB2ADMIN.LOGEINVOICECUSTOMIZEDOPTIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
