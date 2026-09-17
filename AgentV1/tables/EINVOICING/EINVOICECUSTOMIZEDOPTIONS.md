# DB2ADMIN.EINVOICECUSTOMIZEDOPTIONS

- **Module**: `EINVOICING` (high confidence — table name starts with 'EINVOIC')
- **Roles**: `business_data`
- **Columns**: 58
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 199431

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 2 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 3 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 4 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 5 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 6 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 8 | `COMPANYBUSINESSPARTNERNUMBERID` | DECIMAL(8,0) |  | FK | foreign_key |  |
| 9 | `PAUSEMONITORTHREADS` | SMALLINT | NOT NULL |  |  |  |
| 10 | `TAXREGIMECODE` | CHAR(4) |  | FK | foreign_key |  |
| 11 | `TRANSMITTERNUMBERID` | DECIMAL(8,0) |  | FK | foreign_key |  |
| 12 | `TRANSMITTERPOLICYCODE` | CHAR(20) |  |  |  |  |
| 13 | `AUTOMATICLINESDESCRIPTION` | VARCHAR(200) | NOT NULL |  |  |  |
| 14 | `SALESATTACHMENTS` | SMALLINT | NOT NULL |  |  |  |
| 15 | `LINKEDSPOOLFILETYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `SALESASYNCXMLGENERATION` | SMALLINT | NOT NULL |  |  |  |
| 17 | `SALESATTACHMENTSFILEPATH` | VARCHAR(250) |  |  |  |  |
| 18 | `SALESXMLFILEPATH` | VARCHAR(250) |  |  |  |  |
| 19 | `PURCHASESATTACHMENTSFILEPATH` | VARCHAR(250) |  |  |  |  |
| 20 | `PURCHASESXMLFILEPATH` | VARCHAR(250) |  |  |  |  |
| 21 | `PURCHASESIMPORTFILEPATH` | VARCHAR(250) |  |  |  |  |
| 22 | `REA` | SMALLINT | NOT NULL |  |  |  |
| 23 | `REAOFFICECODE` | CHAR(2) |  | FK | foreign_key |  |
| 24 | `REANUMBER` | CHAR(20) |  |  |  |  |
| 25 | `REASHARECAPITAL` | DECIMAL(14,2) |  |  |  |  |
| 26 | `REAUNIQUEPARTNER` | SMALLINT | NOT NULL |  |  |  |
| 27 | `REALIQUIDATION` | SMALLINT | NOT NULL |  |  |  |
| 28 | `MAXRETRIES` | INTEGER | NOT NULL |  |  |  |
| 29 | `STOPONSENDINGERRORS` | SMALLINT | NOT NULL |  |  |  |
| 30 | `ATOAUTHURL` | VARCHAR(250) |  |  |  |  |
| 31 | `ATIXFEBASEURL` | VARCHAR(250) |  |  |  |  |
| 32 | `ATAOOUID` | VARCHAR(100) |  |  |  |  |
| 33 | `ATUOUID` | CHAR(10) |  |  |  |  |
| 34 | `ATCLIENTID` | VARCHAR(100) |  |  |  |  |
| 35 | `ATCLIENTSECRETENCRYPTED` | VARCHAR(100) |  |  |  |  |
| 36 | `ATUSERNAME` | CHAR(30) |  |  |  |  |
| 37 | `ATPASSWORDENCRYPTED` | VARCHAR(60) |  |  |  |  |
| 38 | `ATDEVICETOKENENCRYPTED` | VARCHAR(1500) |  |  |  |  |
| 39 | `ATCONNECTTIMEOUT` | INTEGER | NOT NULL |  |  |  |
| 40 | `ATREADTIMEOUT` | INTEGER | NOT NULL |  |  |  |
| 41 | `ATTOKENRENEWALADVANCESECONDS` | INTEGER | NOT NULL |  |  |  |
| 42 | `ATLOGINATTEMPTS` | INTEGER | NOT NULL |  |  |  |
| 43 | `ATLOGINRETRYDELAYMS` | INTEGER | NOT NULL |  |  |  |
| 44 | `ATTRANSNOTIFICATIONSBATCHCOUNT` | INTEGER | NOT NULL |  |  |  |
| 45 | `ATRECNOTIFICATIONSBATCHCOUNT` | INTEGER | NOT NULL |  |  |  |
| 46 | `ATTRANSLASTNOTIFICATIONID` | CHAR(50) |  |  |  |  |
| 47 | `ATRECLASTNOTIFICATIONID` | CHAR(50) |  |  |  |  |
| 48 | `ICSERVICEURL` | VARCHAR(250) |  |  |  |  |
| 49 | `ICSERVICEPARTNERID` | VARCHAR(100) |  |  |  |  |
| 50 | `ICSERVICEUSERNAME` | CHAR(30) |  |  |  |  |
| 51 | `ICPASSWORDENCRYPTED` | VARCHAR(60) |  |  |  |  |
| 52 | `ICPURCHASESPDFFILEPATH` | VARCHAR(250) |  |  |  |  |
| 53 | `ICPURCHASESZIPFILEPATH` | VARCHAR(250) |  |  |  |  |
| 54 | `ICCONNECTTIMEOUT` | INTEGER | NOT NULL |  |  |  |
| 55 | `ICREADTIMEOUT` | INTEGER | NOT NULL |  |  |  |
| 56 | `ICSALESLASTNOTIFICATIONID` | BIGINT | NOT NULL |  |  |  |
| 57 | `ICPURCHASESLASTNOTIFICATIONID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSLINKEDSPOOLFILETYPE_LINKEDSPOOLFILETYPE` | `LINKEDSPOOLFILETYPECODE` | [`ABSLINKEDSPOOLFILETYPE`](../PLATFORM/ABSLINKEDSPOOLFILETYPE.md) | `CODE` | RESTRICT | `EINVOICECUSTOMIZEDOPTIONS.LINKEDSPOOLFILETYPECODE = ABSLINKEDSPOOLFILETYPE.CODE` |
| `BUSINESSPARTNER_COMPANYBUSINESSPARTNER` | `COMPANYBUSINESSPARTNERNUMBERID` | [`BUSINESSPARTNER`](../FINANCE/BUSINESSPARTNER.md) | `NUMBERID` | RESTRICT | `EINVOICECUSTOMIZEDOPTIONS.COMPANYBUSINESSPARTNERNUMBERID = BUSINESSPARTNER.NUMBERID` |
| `BUSINESSPARTNER_TRANSMITTER` | `TRANSMITTERNUMBERID` | [`BUSINESSPARTNER`](../FINANCE/BUSINESSPARTNER.md) | `NUMBERID` | RESTRICT | `EINVOICECUSTOMIZEDOPTIONS.TRANSMITTERNUMBERID = BUSINESSPARTNER.NUMBERID` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EINVOICECUSTOMIZEDOPTIONS.COMPANYCODE = COMPANY.CODE` |
| `ITALIANDISTRICT_REAOFFICE` | `REAOFFICECODE` | [`ITALIANDISTRICT`](../EINVOICING/ITALIANDISTRICT.md) | `CODE` | RESTRICT | `EINVOICECUSTOMIZEDOPTIONS.REAOFFICECODE = ITALIANDISTRICT.CODE` |
| `TAXREGIME_TAXREGIME` | `TAXREGIMECODE` | [`TAXREGIME`](../EINVOICING/TAXREGIME.md) | `CODE` | RESTRICT | `EINVOICECUSTOMIZEDOPTIONS.TAXREGIMECODE = TAXREGIME.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EINVOICECUSTOMIZEDOPTIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID,
       t.COMPANYBUSINESSPARTNERNUMBERID,
       t.PAUSEMONITORTHREADS,
       t.TAXREGIMECODE,
       t.TRANSMITTERNUMBERID
FROM   DB2ADMIN.EINVOICECUSTOMIZEDOPTIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
